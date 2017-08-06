from ..models import (
    Subject as SubjectModel
)

from graphene import Schema, ObjectType, List
from graphene_sqlalchemy import SQLAlchemyObjectType


class Subject(SQLAlchemyObjectType):
    class Meta:
        model = SubjectModel


class Query(ObjectType):
    subjects = List(Subject)

    def resolve_subjects(self, args, context, info):
        query = Subject.get_query(context)
        return query.all()

schema = Schema(query=Query)
