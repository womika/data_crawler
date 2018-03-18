from bs4 import BeautifulSoup
import requests
import pickle
import json


def get_medical_institutions(doctor_speciality, location):
    url = f'https://www.znanylekarz.pl/{doctor_speciality}/{location}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    search_results = soup.find(attrs={'data-id': "search-results-container"})
    result = []
    for tag in search_results.ul.find_all(attrs={'data-id': "rank-element"}):
        name = tag.find(attrs={'itemprop': 'name'})
        tag.attrs.update({'name': name.text})
        nearest_date = tag.find(class_="rank-element-nearest-date")
        medical_specialty = tag.find_all('meta')
        institution = tag.find('span', class_="name")
        for meta in medical_specialty:
            tag.attrs.update({meta['itemprop']: meta['content']})
        record = {}
        record.update({
            'address': {
                'lat': tag.get('data-object-lat'),
                'lon': tag.get('data-object-lon'),
                'street': tag.get('streetAddress'),
                'city': tag.get('addressLocality'),
                'region': tag.get('addressRegion'),
                'institution': institution.text,
            },
            'doctor': {
                'name': tag.get('name'),
                'type': tag.get('data-object-type'),
                'speciality': tag.get('MedicalSpecialty') or doctor_speciality
            },
            'nearest_date': nearest_date.attrs.get('data-nearest-available-date')
        })
        result.append(record)
    return result
