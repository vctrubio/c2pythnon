import os
import sys

from typing import List, Optional
from dataclasses import field
import json
from rich import print
from pydantic import BaseModel

from sqlalchemy import Column, Float, String, Integer
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session, sessionmaker

Base = declarative_base()


def create_database():
    engine = create_engine("sqlite:///weather.db")
    Base.metadata.create_all(bind=engine)
    return engine


class Location(BaseModel):
    latitude: float = 0
    longitude: float = 0
    address: str = field(default=None)
    days: List['Day']

    def print_all_days(self):
        for day in self.days:
            print(day)


class LocationDB(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    # unique doesnt do shit
    address = Column(String, nullable=False, unique=True)
    days = relationship('DayDB', back_populates='location')

    def print_days(self):
        print(f'Address: {self.address}: Days: {len(self.days)}')
        for day in self.days:
            day.print_attributes()


class Day(BaseModel):
    datetime: str
    feelslike: float
    tempmin: float
    tempmax: float
    precip: float
    precipprob: int
    conditions: str
    moonphase: float


class DayDB(Base):
    __tablename__ = 'days'

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(String)
    conditions = Column(String, nullable=True)
    feelslike = Column(Float)
    tempmin = Column(Float)
    tempmax = Column(Float)
    precip = Column(Float, nullable=True)
    precipprob = Column(Integer, nullable=True)
    moonphase = Column(Float, nullable=True)
    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship('LocationDB', back_populates='days')

    def print_attributes(self):
        attributes = [f'{attr}: {value}' for attr,
                      value in self.__dict__.items() if not attr.startswith('_')]
        print(', '.join(attributes))


def parse_location_data(data):
    location_json = {
        'latitude': data['latitude'],
        'longitude': data['longitude'],
        'address': data['resolvedAddress'],
        'days': [Day(**ptr) for ptr in data['days']]
    }
    location = Location(**location_json)
    return location


def parse_location_db(location, SessionLocal):
    with SessionLocal() as db:
        location_dict = location.model_dump()
        location_dict['days'] = [DayDB(**day.model_dump())
                                 for day in location.days]
        existing_location = db.query(LocationDB).filter_by(
            address=location_dict['address']).first()
        if existing_location is None:
            location_db = LocationDB(**location_dict)
            db.add(location_db)
            print(f'location {location.address} added to database ...!')
        else:
            for day in location.days:
                existing_day = db.query(DayDB).filter_by(
                    datetime=day.datetime).first()
                if existing_day is None:
                    day_db = DayDB(**day.model_dump())
                    existing_location.days.append(day_db)
                    print(f'day {day.datetime} added to database ...!')
        db.commit()
        print(f'location {location.address} looper done ...!')


def open_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        return data


def init():
    directory_path = '../json_data/'
    files = os.listdir(directory_path)
    json_files = [f for f in files if f.endswith('.json')]
    data = []
    for file in json_files:
        ptr = open_file(directory_path + file)
        data.append(ptr)

    return data if len(data) > 0 else sys.exit('EXIT: no json files found')


def create_session_local():
    engine = create_database()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal


if __name__ == '__main__':
    data_to_parse = init()
    SessionLocal = create_session_local()
    for data in data_to_parse:
        location = parse_location_data(data)
        parse_location_db(location, SessionLocal)

    # with SessionLocal() as db:
    #     print_days = db.query(LocationDB).all()
    #     # print_days = db.query(LocationDB).filter_by(
    #     #     address='Lisboa, Portugal').all()
    #     for i in print_days:
    #         i.print_days()
