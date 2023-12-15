from dataclasses import dataclass, field
from typing import List

import json
import os


API_FETCH_DIR = './api_fetch/'
# files_to_scrap = ['location.json']
files_to_scrap = ['day.json', 'location.json']

# NOTE _underscores are meant to be imported | _underscore_ is meant to be *inheritate*

@dataclass
class Location:
    id: int = 0
    _latitude: float = 0 #field(default=0, metadata={'unit': 'degrees'})
    _longitude: float = 0
    _address: str = field(default=None)

    
@dataclass
class Day:
    id: int
    _feelslike: float
    _tempmin: float
    _tempmax: float
    _percip: float
    _percipprob: int


@dataclass
class Entity():
    _location_: Location
    _days_: List[Day] = field(default_factory=list)
    _name: str = field(default=None)

    def __post_init__(self):
        self._name = self._location._address
    
    def __str__(self):
        return f"Entity: {self._name} {self._days}"

####################
def get_json() -> dict:
    rtn = {}
    for file_name in files_to_scrap:
        try:
            with open(f'{API_FETCH_DIR}{file_name}', 'r') as file:
                    data = json.load(file)
                    data['_model'] = os.path.splitext(file_name)[0].title()
                    rtn[file_name.upper()] = data
        except FileNotFoundError:
            print(f".!. File {file_name} not found in {os.getcwd()}{API_FETCH_DIR[1::]}")
    return rtn


def if_key_in_class(key, Class):
    search_filter = '_' + key # => in order to match our attributes
    if search_filter in Class.__dict__:
        print(f'debug: yes {key}')
    else:
        print(f'debug: no {key}')
    return search_filter in Class.__dict__

def json_to_class_population(data, Class):
    def iterate_dict(d):
        for key, value in d.items():
            if isinstance(value, dict):
                iterate_dict(value)
            else:
                if_key_in_class(key, Class)

    iterate_dict(data)

if __name__ == '__main__':
    data_from_json = get_json()
    classes = [Location, Day] # (Entity is made by us)
    
    #make zip/pai between json model and class model
    #parse json into models
    print(data_from_json)

    json_to_class_population(data_from_json, Location)


