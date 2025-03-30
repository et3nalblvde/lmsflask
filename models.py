from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # или ваш URI для базы данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f'<Department {self.name}>'

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=True)
    department = db.relationship('Department', backref=db.backref('works', lazy=True))

    def __repr__(self):
        return f'<Work {self.title}>'

if __name__ == "__main__":
    db.create_all()
