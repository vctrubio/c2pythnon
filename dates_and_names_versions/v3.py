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
    _latitude: float = 0  # field(default=0, metadata={'unit': 'degrees'})
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
            print(
                f".!. File {file_name} not found in {os.getcwd()}{API_FETCH_DIR[1::]}")
    return rtn


def if_key_in_class(key, Class):
    search_filter = '_' + key  # => in order to match our attributes
    if search_filter in Class.__dict__:
        print(f'debug: yes {key}')
    else:
        print(f'debug: no {key}')
    return search_filter in Class.__dict__


def if_key_in_class_model_name(key, model_name):
    # search_filter = key[1:]
    search_filter = key
    print(f'debug: model_name {search_filter} :vs: {model_name}')
    return search_filter in model_name


def json_to_class_population(data, Class):
    def iterate_dict(d):
        for key, value in d.items():
            if isinstance(value, dict):
                iterate_dict(value)
            else:
                if_key_in_class(key, Class)

    iterate_dict(data)

# parse json into models


def parse_json_into_models(data_from_json):
    class_constructor = []
    to_import = [Location]
    # to_import = [Location, Day]
    class_names = [cls.__name__ for cls in to_import]

    for _, values in data_from_json.items():
        if '_model' in values:
            if (values['_model']) in class_names:
                class_constructor.append(values)
                # print('yes')
                # print(f'OK: {values["_model"]} in ')

    for it in class_constructor:
        try:
            cls = globals()[it['_model']]
            class_attrs = cls.__match_args__
            filter_dict_keys = {}
            for attr in class_attrs:
                if attr.startswith('_'):
                    attr_trim = attr[1:]
                    if attr_trim in it:
                        filter_dict_keys[attr_trim] = it[attr_trim]
            print(filter_dict_keys)
        except KeyError:
            print(
                f'KeyError: {it["_model"]} not found in globals() | SOMETHING WENT WRONG')

        # clean unecesrray keys
        # call constructor as dict


if __name__ == '__main__':
    data_from_json = get_json()
    constructor = parse_json_into_models(data_from_json)

#    print(data_from_json)
#    json_to_class_population(data_from_json, Location)


#    print(Location.__name__)
