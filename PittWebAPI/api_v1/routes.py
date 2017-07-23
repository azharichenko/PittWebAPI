from . import api
from ..models import Subject

from flask_restful import Resource, Api

rest_api = Api(api)


class SubjectList(Resource):
    def get(self):
        subjects = Subject.query.all()
        return [subject.to_dict() for subject in subjects]

rest_api.add_resource(SubjectList, '/subjects')
