from ..models import Subject
from .subjects import populate_database


def populate():
    populate_database(Subject)
