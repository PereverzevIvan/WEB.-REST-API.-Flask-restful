from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.models.jobs import Jobs
from data.parsers.jobs_reqparse import parser


def errors_with_jobs(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Users {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        if type(job_id) != int:
            return jsonify({'error': 'Bad request'})
        errors_with_jobs(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(
            only=('id', 'job', 'work_size', 'collaborators', 'start_date',
                  'end_start', 'is_finished', 'team_leader'))})

    def delete(self, job_id):
        if type(job_id) != int:
            return jsonify({'error': 'Bad request'})
        errors_with_jobs(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id', 'job', 'work_size', 'collaborators', 'start_date',
                  'end_start', 'is_finished', 'team_leader')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            id=args['id'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished'],
            team_leader=args['team_leader'])
        if args['start_date']:
            job.start_date = args['start_date']
        if args['end_start']:
            job.end_start = args['end_start']
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
