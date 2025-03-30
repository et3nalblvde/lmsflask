from flask_restful import reqparse


job_parser = reqparse.RequestParser()
job_parser.add_argument('title', type=str, required=True, help='Title is required')
job_parser.add_argument('description', type=str, required=True, help='Description is required')
