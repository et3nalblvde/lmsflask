from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mars_one.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Инициализация flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# Модель пользователя
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)


# Модель работы
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)


# Загрузка пользователя
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Главная страница (показ работ)
@app.route("/")
@app.route("/home")
@login_required
def home():
    tasks = Task.query.all()
    return render_template("home.html", tasks=tasks)


# Страница авторизации
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:  # Здесь должен быть хэшированный пароль
            login_user(user)
            return redirect(url_for("home"))
        else:
            flash("Неверные данные для входа. Попробуйте снова.")

    return render_template("login.html")


# Страница регистрации
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


# Страница добавления работы
@app.route("/add_task", methods=["GET", "POST"])
@login_required
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]

        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        flash("Работа успешно добавлена!")
        return redirect(url_for("home"))

    return render_template("add_task.html")


# Выход из системы
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
