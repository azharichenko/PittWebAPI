from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import (scoped_session, sessionmaker, backref, relationship)
from .database import Base, db_session


class Term(Base):
    __tablename__ = 'term'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True)

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


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    term_id = Column(Integer, ForeignKey('term.id'))
    term = relationship(
        Term,
        backref=backref('term',
                        uselist=True,
                        cascade='delete,all')
    )

    @staticmethod
    def register(code, name, term):
        subject = Subject(
            code=code,
            name=name,
            term=term
        )
        db_session.add(subject)
        db_session.commit()

    @staticmethod
    def register_all(subject_codes, term):
        for code in subject_codes:
            name, code = code
            Subject.register(name=name, code=code, term=term)

    def __repr__(self):
        return 'Subject({})'.format(self.code)


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(Integer)

    subject_id = Column(Integer, ForeignKey('subject.id'))
    subject = relationship(
        Subject,
        backref=backref('subject',
                        uselist=True,
                        cascade='delete,all')
    )

    def __repr(self):
        return 'Course({} {})'.format(self.subject, self.number)


class Section(Base):
    __tablename__ = 'section'
    id = Column(Integer, primary_key=True)


class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)


class Building(Base):
    __tablename__ = 'building'
    id = Column(Integer, primary_key=True)


class Classroom(Base):
    __tablename__ = 'classroom'
    id = Column(Integer, primary_key=True)


class Textbook(Base):
    __tablename__ = 'textbook'
    id = Column(Integer, primary_key=True)


class Instructor(Base):
    __tablename__ = 'instructor'
    id = Column(Integer, primary_key=True)
