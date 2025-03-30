from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mars_one.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator = db.relationship('User', backref=db.backref('tasks', lazy=True))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
@app.route("/home")
@login_required
def home():
    tasks = Task.query.all()
    return render_template("home.html", tasks=tasks)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return redirect(url_for("home"))
        else:
            flash("Неверные данные для входа. Попробуйте снова.")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]

        # Проверка на существующего пользователя
        if User.query.filter_by(username=username).first():
            flash("Пользователь с таким именем уже существует.")
        else:
            new_user = User(username=username, password=password, first_name=first_name, last_name=last_name)
            db.session.add(new_user)
            db.session.commit()
            flash("Регистрация успешна! Пожалуйста, войдите.")
            return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/add_department", methods=["GET", "POST"])
@login_required
def add_department():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]

        new_department = Department(name=name, description=description)
        db.session.add(new_department)
        db.session.commit()
        flash("Департамент успешно добавлен!")
        return redirect(url_for("list_departments"))

    return render_template("add_department.html")


@app.route("/edit_department/<int:department_id>", methods=["GET", "POST"])
@login_required
def edit_department(department_id):
    department = Department.query.get_or_404(department_id)

    if request.method == "POST":
        department.name = request.form["name"]
        department.description = request.form["description"]
        db.session.commit()
        flash("Департамент успешно обновлен!")
        return redirect(url_for("list_departments"))

    return render_template("edit_department.html", department=department)


@app.route("/departments")
@login_required
def list_departments():
    departments = Department.query.all()
    return render_template("list_departments.html", departments=departments)


@app.route("/add_task", methods=["GET", "POST"])
@login_required
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        category_ids = request.form.getlist("categories")

        new_task = Task(title=title, description=description, creator_id=current_user.id)

        # Связываем задачу с выбранными категориями
        for category_id in category_ids:
            category = Category.query.get(category_id)
            new_task.categories.append(category)

        db.session.add(new_task)
        db.session.commit()
        flash("Работа успешно добавлена!")
        return redirect(url_for("home"))

    categories = Category.query.all()
    return render_template("add_task.html", categories=categories)


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if task.creator_id != current_user.id and current_user.id != 1:
        flash("У вас нет прав на редактирование этой работы.")
        return redirect(url_for("home"))

    if request.method == "POST":
        task.title = request.form["title"]
        task.description = request.form["description"]

        db.session.commit()
        flash("Работа успешно обновлена!")
        return redirect(url_for("home"))

    return render_template("edit_task.html", task=task)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
