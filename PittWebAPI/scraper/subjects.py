import requests
import grequests
from bs4 import BeautifulSoup

LETTERS = 'ABCDEFGHIJLMNOPRSTUW'
TO_BE_DETERMINED = 'KQV'  # TODO(Alex Z.) Look into ... to help assist with this

CATALOG_URL = 'https://psmobile.pitt.edu/app/catalog/listCatalog'
BASE_URL = 'https://psmobile.pitt.edu/app/catalog/listSubjects'


# TODO(Alex Z.) Be able to fetch direct from course catalog
# def _fetch_catalog_letters():
#     response = requests.get(CATALOG_URL)
#     soup = BeautifulSoup(response.text, 'lxml')
#     return soup


def _fetch_all_departments():
    urls = [grequests.get(BASE_URL + char) for char in LETTERS]
    return grequests.map(urls)


def _extract_subjects(tags):
    subjects = [
        tuple(tag.text.split(' - '))
        for tag in tags
    ]
    return subjects


def _parse_subjects(responses):
    subject_catalog = []
    for response in responses:
        soup = BeautifulSoup(response.text, 'lxml')
        parent = soup.find('div', {'class', 'primary-head'}).parent
        subjects = parent.findAll('div', {'class': 'strong section-body'})
        subject_catalog.extend(_extract_subjects(subjects))
    return subject_catalog


def populate_database(model):
    responses = _fetch_all_departments()
    subject_codes = _parse_subjects(responses)
    model.register_all(subject_codes)
