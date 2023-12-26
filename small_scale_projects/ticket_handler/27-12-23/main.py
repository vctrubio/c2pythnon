from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Annotated, Optional
import model
from db import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
model.Base.metadata.create_all(bind=engine)


class ApiPerson(BaseModel):
    name: str
    # tickets: List['ApiTicket'] = None

class ApiTicket(BaseModel):
    name: str
    price: int
    quantity: int = 1
    paid: bool
    person_id: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post('/tickets/')
async def create_ticket(ticket: ApiTicket, db: db_dependency):
    db_ticket = model.Ticket(**ticket.model_dump())
    # db_ticket = model.Ticket(name=ticket.name, price=ticket.price, quantity=ticket.quantity, paid=ticket.paid)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


@app.get('/')
async def get_tickets(db: db_dependency):
    return db.query(model.Ticket).all()


@app.get('/tickets/{ticket_id}')
async def get_ticket(ticket_id: int, db: db_dependency):
    db_ticket = db.query(model.Ticket).filter(
        model.Ticket.id == ticket_id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail='Ticket not found')
    return db_ticket


@app.delete('/tickets/{ticket_id}')
async def delete_ticket(ticket_id: int, db: db_dependency):
    db_ticket = db.query(model.Ticket).filter(
        model.Ticket.id == ticket_id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail='Ticket not found')
    db.delete(db_ticket)
    db.commit()
    return db_ticket


@app.put('/tickets/{ticket_id}')
async def update_ticket(ticket_id: int, ticket: ApiTicket, db: db_dependency):
    db_ticket = db.query(model.Ticket).filter(
        model.Ticket.id == ticket_id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail='Ticket not found')
    if ticket.name is not None:
        db_ticket.name = ticket.name
    if ticket.price is not None:
        db_ticket.price = ticket.price
    if ticket.quantity is not None:
        db_ticket.quantity = ticket.quantity
    if ticket.paid is not None:
        db_ticket.paid = ticket.paid
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


########### Persons ###########


@app.get('/persons/')
async def get_persons(db: db_dependency):
    return db.query(model.Person).all()


@app.get('/persons/{person_id}')
async def get_person(person_id: int, db: db_dependency):
    db_person = db.query(model.Person).filter(
        model.Person.id == person_id).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail='Person not found')
    return db_person


@app.post('/persons/')
async def create_person(person: ApiPerson, db: db_dependency):
    db_person = model.Person(**person.model_dump())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person
