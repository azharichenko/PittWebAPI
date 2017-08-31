from ..models import (
    Subject as SubjectModel,
    Course as CourseModel
)

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType


class Subject(SQLAlchemyObjectType):
    class Meta:
        model = SubjectModel
        interfaces = (graphene.relay.Node,)


class Course(SQLAlchemyObjectType):
    class Meta:
        model = CourseModel
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    course = graphene.List(Course)
    subject = graphene.Field(Subject)
    subjects = graphene.List(Subject)

    def resolve_subjects(self, args, context, info):
        return Subject.get_query(context).all()

    def resolve_subject(self, args, context, info):
        query = Subject.get_query(context)
        return query.first()

    def resolve_course(self, args, context, info):
        query = Course.get_query(context)
        return query.all()


schema = graphene.Schema(query=Query, types=[Subject, Course])