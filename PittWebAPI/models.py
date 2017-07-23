from . import db


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), index=True, unique=False)
    name = db.Column(db.String(32), unique=False)

    @staticmethod
    def register(code, name):
        subject = Subject(code=code, name=name)
        db.session.add(subject)
        db.session.commit()

    @staticmethod
    def register_all(subject_codes):
        for code in subject_codes:
            Subject.register(*code[:2])  # TODO(Alex Z.) Look into the splitting since - occurs more than once

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name
        }

    def __repr__(self):
        return '<Subject {}>'.format(self.code)

