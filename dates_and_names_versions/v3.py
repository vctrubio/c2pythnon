'''
json_Location

print(entity) = 
{
    "queryCost": 1,
    "latitude": 40.1285,
    "longitude": -5.66042,
    "address": "jarandilla de la vera"
}

json_day = 
{
    "feelslike": 11.4,
    "tempmin": 8.2,
    "tempmax": 17.8,
    "percip": 0.2,
    "percipprob": 100
}
'''

from dataclasses import dataclass, field
from typing import List

@dataclass
class Location:
    id: int = 0
    _latitude: float = 0 #field(default=0, metadata={'unit': 'degrees'})
    _longitude: float = 0
    _address: str = field(init=False)

class Day:
    id: int
    _feelslike: float
    _tempmin: float
    _tempmax: float
    _percip: float
    _percipprob: int


@dataclass
class Entity():
    _location: Location
    _days: List[Day] = field(default_factory=list)
    _name: str = field(init=False)

    def __post_init__(self):
        self._name = self._location._address

if __name__ == '__main__':
    location = Location()
    location._address = "henansanzh"
    entity = Entity(location)
    print(location)
    print(entity)

