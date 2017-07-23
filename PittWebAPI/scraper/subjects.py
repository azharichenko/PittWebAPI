import string
from pprint import pprint

import grequests
from bs4 import BeautifulSoup


ALPHA = string.ascii_uppercase
BASE_URL = 'https://psmobile.pitt.edu/app/catalog/listSubjectsByLetter/UPITT/'


def _fetch_all_departments():
    urls = [grequests.get(BASE_URL + char) for char in ALPHA]
    return grequests.map(urls)


def _parse_subjects(responses):
    for response in responses:
        soup = BeautifulSoup(response.text, 'lxml')
        parent = soup.find('div', {'class', 'primary-head'}).parent
        subjects = parent.findAll('div', {'class': 'strong section-body'})
    pass


responses = _fetch_all_departments()
pprint(responses)
# subject_codes = _parse_subjects(responses)