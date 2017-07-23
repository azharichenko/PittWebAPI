from . import db


class Subjects(db.model):
    id = db.Column(db.INTEGER, primary_key=True)
    code = db.Column(db.String(12), unique=True)
    name = db.Column(db.String(32), unique=True)

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __repr__(self):
        return '<Subject {}>'.format(self.code)


class Course(db.model):
    pass
