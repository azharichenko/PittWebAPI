from ..models import Subject, Term
from ..database import db_session
from .subjects import populate_database


def populate():
    term = Term(number=2194)
    db_session.add(term)
    db_session.commit()
    populate_database(Subject, term)
