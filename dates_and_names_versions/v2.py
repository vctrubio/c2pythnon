from typing import List, Type, Optional
from pydantic import BaseModel


# CLASSES #

class Location(BaseModel):
    long: float
    lat: float
    address: str
    _name: 'Name'

    def __init__(self, long: float, lat: float, address: str):
        super().__init__(long=long, lat=lat, address=address)
        name = self.create_location_and_name()
        self._name = name
        # print(f'__init__ lat {lat}, long {long}, address {address}')

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
    start_date: Optional[str]
    end_date: Optional[str]
    datetime: Optional[str]
    feels_like: float
    precip: float
    ptr_name: 'Name'

    def __init__(self, feels_like: float, precip: float, start_date: str, end_date: str, datetime: str, name: 'Name' = None):
        super().__init__(start_date=start_date, end_date=end_date,
                         datetime=datetime, feels_like=feels_like, precip=precip, ptr_name=name)
        myDay.append(self)
        print("__init__ day: ", self.ptr_name)
    
    def get_name(self):
        return self.ptr_name


class Name(BaseModel):
    name: str
    tmp: int = 22
    location: Location
    days: List[Day] = []

    def day_create(self, feels_like=10, precip=0, start_date=None, end_date=None, datetime=None):
        day = Day(start_date=start_date, end_date=end_date,
                  datetime=datetime, feels_like=feels_like, precip=precip, name = self)
        self.days.append(day)

    def show_all_days(self):
        for i in self.days:
            print(i)


# FTs #
def is_name_in_list(name_to_check, name_list):
    # need to check also for lat and long to make sure its the same
    return next((name for name in name_list if name_to_check == name.name), None)
    # for indx, i in enumerate(name_list):
    #     if name_to_check == i.name:
    #         return name_list[indx]


# DB #
myLocation = []
myName = []
myDay = []

'''
A location has one Name
A name has many days
Days belong to name
'''

if __name__ == '__main__':
    print('run')

    location = Location(long=2.2, lat=4.2, address='villa')

    name = location.get_name()
    # name.day_create(feels_like=22, precip=0.2, datetime='10/12/2022')
    # name.day_create(feels_like=21, datetime='12/12/2022')
    # name.day_create()
    # name.show_all_days()

    nd = Day(22,10,None,None,None,name)
    print(myDay)

