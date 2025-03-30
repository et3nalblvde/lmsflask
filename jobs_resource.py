from flask_restful import Resource
from flask import request
from models import Job
from args_parser import job_parser


class JobsResource(Resource):
    """Ресурс для работы с одной работой"""

    def get(self, job_id):

        job = Job.query.get(job_id)
        if not job:
            return {'message': 'Job not found'}, 404
        return job.to_dict(), 200

    def put(self, job_id):

        job = Job.query.get(job_id)
        if not job:
            return {'message': 'Job not found'}, 404

        data = job_parser.parse_args()
        job.title = data['title']
        job.description = data['description']
        job.save()
        return job.to_dict(), 200

    def delete(self, job_id):
        """Удалить работу по ID"""
        job = Job.query.get(job_id)
        if not job:
            return {'message': 'Job not found'}, 404

        job.delete()
        return {'message': 'Job deleted'}, 200


class JobsListResource(Resource):


    def get(self):
        """Получить список всех работ"""
        jobs = Job.query.all()
        return {'jobs': [job.to_dict() for job in jobs]}, 200

    def post(self):

        data = job_parser.parse_args()
        new_job = Job(
            title=data['title'],
            description=data['description']
        )
        new_job.save()
        return new_job.to_dict(), 201
