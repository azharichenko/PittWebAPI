from ..models import (
    Subject as SubjectModel
)

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType


class Subject(SQLAlchemyObjectType):
    class Meta:
        model = SubjectModel
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    subjects = graphene.List(Subject)

    def resolve_subjects(self, args, context, info):
        query = Subject.get_query(context)
        return query.all()

schema = graphene.Schema(query=Query)
