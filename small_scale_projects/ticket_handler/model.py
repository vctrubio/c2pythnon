from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from db import Base


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    paid = Column(Boolean, nullable=False, default=False)
    # user_id = Column(Integer, ForeignKey('persons.id'))

    def __repr__(self):
        return f'<Ticket {self.id} {self.title} {self.description} {self.done} {self.user_id}>'


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    tickets = Column(Integer, ForeignKey('tickets.id'))

    def __repr__(self):
        return f'<Person {self.id} {self.name} {self.tickets}>'
