import os
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, backref, relationship)
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
    name = Column(String)
    code = Column(String)

    @staticmethod
    def register(code, name):
        subject = Subject(code=code, name=name)
        course = Course(name='0100' + code, subject=subject)
        course1 = Course(name='0200' + code, subject=subject)
        course2 = Course(name='0300' + code, subject=subject)
        db_session.add(subject)
        db_session.add(course)
        db_session.add(course1)
        db_session.add(course2)
        db_session.commit()

    @staticmethod
    def register_all(subject_codes):
        for code in subject_codes:
            Subject.register(*code[:2])  # TODO(Alex Z.) Look into the splitting since - occurs more than once

    def __repr__(self):
        return 'Subject({})'.format(self.code)


class Term(Base):
    __tablename__ = 'term'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)

    @staticmethod
    def register(number):
        term = Term(number)
        db_session.add(term)
        db_session.commit()

    @staticmethod
    def register_all(term_numbers):
        for number in term_numbers:
            Term.register(number)

    def __repr__(self):
        return 'Term({})'.format(self.number)


class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)


class Classroom(Base):
    __tablename__ = 'classroom'
    id = Column(Integer, primary_key=True)
    

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    subject_id = Column(Integer, ForeignKey('subject.id'))
    subject = relationship(
        Subject,
        backref=backref('subject',
                        uselist=True,
                        cascade='delete,all')
    )


class Textbook(Base):
    __tablename__ = 'textbook'
    id = Column(Integer, primary_key=True)
