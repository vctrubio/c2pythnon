from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from db import Base
from sqlalchemy.orm import relationship


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    paid = Column(Boolean, nullable=False, default=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    # person = relationship("Person", back_populates="tickets")

    def __repr__(self):
        return f'<Ticket {self.id} {self.title} {self.description} {self.done} {self.user_id}>'


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    tickets = relationship("Ticket", back_populates="person")

    def __repr__(self):
        return f'<Person {self.id} {self.name} {self.tickets}>'
