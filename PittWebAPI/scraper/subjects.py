import string
import requests

from bs4 import BeautifulSoup


CATALOG_URL = 'https://psmobile.pitt.edu/app/catalog/listCatalog'
BASE_URL = 'https://psmobile.pitt.edu/app/catalog/listSubjectsByLetter/UPITT/'


# TODO(Alex Z.) Be able to fetch direct from course catalog
# def _fetch_catalog_letters():
#     response = requests.get(CATALOG_URL)
#     soup = BeautifulSoup(response.text, 'lxml')
#     return soup


def _fetch_all_departments(): 
    responses = []
    for char in string.ascii_uppercase:
            r = requests.get(BASE_URL + char)
            if not 'There are no subjects' in r.text:
                responses.append(r)
        
    return responses


def _extract_subjects(tags):
    subjects = [
        tuple(tag.text.split(' - '))
        for tag in tags
    ]
    return subjects[:2]


def _parse_subjects(responses):
    subject_catalog = []
    for response in responses:
        try:
            soup = BeautifulSoup(response.text, 'lxml')
            parent = soup.find('div', {'class', 'primary-head'}).parent
            subjects = parent.findAll('div', {'class': 'strong section-body'})
            subject_catalog.extend(_extract_subjects(subjects))
        except AttributeError:
            pass
    return subject_catalog


def populate_database(model, term):
    responses = _fetch_all_departments()
    subject_codes = _parse_subjects(responses)
    model.register_all(subject_codes, term)
