from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, current_user, login_required, logout_user
from app import app, db, bcrypt
from models import User, Task
from forms import RegistrationForm, LoginForm, AddTaskForm

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/add_task", methods=['GET', 'POST'])
@login_required
def add_task():
    form = AddTaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            deadline=form.deadline.data,
            priority=form.priority.data,
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully', 'success')
        return redirect(url_for('index'))
    return render_template('add_task.html', form=form)

@app.route("/")
@app.route("/index")
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)
