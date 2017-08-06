#!/usr/bin/env python
import argparse

from PittWebAPI import create_app
from PittWebAPI.models import Base, engine

parser = argparse.ArgumentParser(description='Pitt WebAPI Server')
parser.add_argument('-d', '--dev', action='store_true')
parser.add_argument('-t', '--testing', action='store_true')

args = parser.parse_args()
configuration = ''
if args.dev:
    configuration = 'development'
elif args.testing:
    configuration = 'testing'
else:
    configuration = 'production'

if __name__ == '__main__':
    app = create_app(configuration)
    with app.app_context():
        Base.metadata.create_all(bind=engine)

        from PittWebAPI.scraper import populate
        populate()

    app.run()
