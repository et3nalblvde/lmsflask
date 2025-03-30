from flask_restful import reqparse

user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_parser.add_argument('email', type=str, required=True, help="Email cannot be blank")
user_parser.add_argument('age', type=int, required=True, help="Age cannot be blank")
user_parser.add_argument('city_from', type=str, required=True, help="City from cannot be blank")
