import os
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    os.path.dirname(__file__), '../data-dev.sqlite3'
)

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    code = Column(String(32), index=True, unique=False)
    name = Column(String(32), unique=False)

    def __init__(self, code, name):
        self.code = code
        self.name = name

    @staticmethod
    def register(code, name):
        subject = Subject(code=code, name=name)
        db_session.add(subject)
        db_session.commit()

    @staticmethod
    def register_all(subject_codes):
        for code in subject_codes:
            Subject.register(*code[:2])  # TODO(Alex Z.) Look into the splitting since - occurs more than once

    def __repr__(self):
        return '<Subject {}>'.format(self.code)


class Term(Base):
    __tablename__ = 'term'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True)


class Class(Base):
    __tablename__ = 'class'


class Textbook(Base):
    __tablename__ = 'textbook'
