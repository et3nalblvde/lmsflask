from flask import Blueprint, jsonify, request, abort
from models import db, User

users_api = Blueprint('users_api', __name__)

@users_api.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])



@users_api.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user.to_dict())



@users_api.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'age' not in data or 'city_from' not in data:
        abort(400, description="Missing required fields")

    new_user = User(
        name=data['name'],
        email=data['email'],
        age=data['age'],
        city_from=data['city_from']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201



@users_api.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")

    data = request.get_json()

    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    if 'age' in data:
        user.age = data['age']
    if 'city_from' in data:
        user.city_from = data['city_from']

    db.session.commit()

    return jsonify(user.to_dict())



@users_api.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": f"User {user_id} deleted"}), 200
