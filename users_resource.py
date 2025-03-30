from flask_restful import Resource
from flask import request
from models import User, db
from parsers import user_parser

class UsersListResource(Resource):
    def get(self):
        users = User.query.all()
        result = []
        for user in users:
            result.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'age': user.age,
                'city_from': user.city_from
            })
        return {'users': result}, 200

    def post(self):
        args = user_parser.parse_args()
        new_user = User(
            name=args['name'],
            email=args['email'],
            age=args['age'],
            city_from=args['city_from']
        )
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created', 'id': new_user.id}, 201


class UsersResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'age': user.age,
            'city_from': user.city_from
        }, 200

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        args = user_parser.parse_args()
        user.name = args['name']
        user.email = args['email']
        user.age = args['age']
        user.city_from = args['city_from']
        db.session.commit()
        return {'message': 'User updated'}, 200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted'}, 200
