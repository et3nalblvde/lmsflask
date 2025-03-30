from flask import Flask
from models import db
from users_api import users_api
from views import views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.register_blueprint(users_api)
app.register_blueprint(views)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
