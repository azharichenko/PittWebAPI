from ..models import (
    Subject as SubjectModel
)

from graphene import relay, Schema, ObjectType
from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
    SQLAlchemyConnectionField
)


class Subject(SQLAlchemyObjectType):
    class Meta:
        model = SubjectModel
        interfaces = (relay.Node,)


class Query(ObjectType):
    node = relay.Node.Field()
    all_subjects = SQLAlchemyConnectionField(Subject)


schema = Schema(query=Query)
