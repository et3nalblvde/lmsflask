from flask import Flask, render_template, request, redirect, url_for, flash
from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib

app = Flask(__name__)
app.secret_key = "12345"


DATABASE_URL = "sqlite:///mars_explorer.sqlite"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        age = int(request.form['age'])
        position = request.form['position']
        speciality = request.form['speciality']
        address = request.form['address']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']


        if password != confirm_password:
            flash("Пароли не совпадают!", 'danger')
            return redirect(url_for('register'))


        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()


        new_user = User(surname=surname, name=name, age=age, position=position,
                        speciality=speciality, address=address, email=email, hashed_password=hashed_password)


        session.add(new_user)
        session.commit()

        flash("Регистрация успешна!", 'success')
        return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
