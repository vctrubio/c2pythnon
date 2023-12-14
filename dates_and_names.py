import json

from typing import List
from pydantic import BaseModel, validator


# CLASSES #

class Location(BaseModel):
    long: float
    lat: float
    address: str
    _name: 'Name'

    def __init__(self, long: float, lat: float, address: str):
        # print(f'__init__ lat {lat}, long {long}, address {address}')
        super().__init__(long=long, lat=lat, address=address)
        name = self.create_location_and_name()
        self._name = name
        myLocation.append(self)

    #when location is created, call function to see if Name is present, if not create one and return Name
    def create_location_and_name(self):
        if is_name_in_list(self.address, myName):
            return is_name_in_list(self.address, myName)
        else:
            name = Name(name=self.address, location=self)
            myName.append(name)
            return name
    
    def get_name(self):
        return self._name


class Day(BaseModel):
    start_date: str = None
    end_date: str = None
    def_date: str = None
    feels_like: float
    percip: float


class Name(BaseModel):
    name: str
    tmp: int = 22
    location: Location
    days: List[Day] = []

    def day_create(self, start_date, end_date, feels_like, percip):
        print(f'start_date: {start_date}, end_date: {end_date}, feels_like: {feels_like}, percip: {percip}')


#CRUD days

# FTs #
def is_name_in_list(name_to_check, name_list):
    # for indx, i in enumerate(name_list):
    #     if name_to_check == i.name:
    #         return name_list[indx]
    return next((name for name in name_list if name_to_check == name.name), None) ##need to check also for lat and long to make sure its the same

# DB #
myLocation = []
myName = []
myDay = []




if __name__ == '__main__':
    print('run')

    location = Location(long=2.2, lat=4.2, address='villa')

    name = location.get_name()
    print(name)
    name.day_create('10.12', '13.12', '12', '22')

    # print(myName)
    # print(myLocation)


#when we create a new Location, check to see if the name exist in Name class, if not create a new class
#append new class to list of classes

#from name, create days to create data
