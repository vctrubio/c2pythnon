from dataclasses import Field
from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Category(Enum):
    JARDIN = "jardin"
    GASOIL = "gasoil"
    MAISON = "maison"

class Ticket(BaseModel):
    name: str  # = Field(unique=True)
    price: float
    category: Category


# create seeds
ticket1 = Ticket(name="ticket1", price=10.0, category=Category.JARDIN)
ticket2 = Ticket(name="ticket2", price=10.0, category=Category.GASOIL)
ticket3 = Ticket(name="ticket3", price=30.0, category=Category.MAISON)
ticket4 = Ticket(name="ticket4", price=40.0, category=Category.JARDIN)
ticket5 = Ticket(name="ticket5", price=50.0, category=Category.GASOIL)
ticket6 = Ticket(name="ticket6", price=60.0, category=Category.MAISON)

tickets = {
    0: ticket1,
    1: ticket2,
    2: ticket3,
    3: ticket4,
    4: ticket5,
    5: ticket6
}
# print(tickets[2])


@app.get("/")
def index():
    return {"tickets-": tickets}


@app.get("/tickets/{ticket_id}")
def query_by_id(ticket_id: int) -> Ticket:
    if ticket_id not in tickets:
        raise HTTPException(
            status_code=404, detail=f"Ticket not found. ID {ticket_id}")
    return tickets[ticket_id]


# we can query tickets like this /tickets?price=20
Selection = dict[
    str, str | int | float | Category | None
]  # dictionary containing the user's query arguments


@app.get("/tickets/")
def query_ticket_by_param(
    name: str | None = None,
    price: float | None = None,
    category: Category | None = None
):
    def check_ticket(ticket: Ticket) -> bool:
        return all(
            (
                name is None or ticket.name == name,
                price is None or ticket.price == price,
                category is None or ticket.category == category
            )
        )
    selection = [ticket for ticket in tickets.values() if check_ticket(ticket)]
    return {
        "query": {
            "name": name,
            "price": price,
            "category": category
        },
        "selection": {ticket.name: ticket for ticket in selection}
    }
# print(query_ticket_by_param(name="ticket1"))


@app.post("/ticket_post/")
def create_ticket(ticket: Ticket):
    if ticket.name in [ticket.name for ticket in tickets.values()]:
        raise HTTPException(
            status_code=400, detail=f"Ticket already exists. Name {ticket.name}")
    tickets[len(tickets)] = ticket
    return ticket

#update
@app.put("/tickets/{ticket_id}")
def update(
    ticket_id: int,
    name: str | None = None,
    price: float | None = None,
    category: Category | None = None
    ):
    if ticket_id not in tickets:
        raise HTTPException(
            status_code=404, detail=f"Ticket not found. ID {ticket_id}")
    if all(info is None for info in (name, price, category)):
        raise HTTPException(
            status_code=400, detail=f"No Paramas to update. ID {ticket_id}")
    
    ticket = tickets[ticket_id]
    if name is not None:
        ticket.name = name
    if price is not None:
        ticket.price = price
    if category is not None:
        ticket.category = category
    return {"updated_ticket": ticket}

#delete
@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    if ticket_id not in tickets:
        raise HTTPException(
            status_code=404, detail=f"Ticket not found. ID {ticket_id}")
    # del tickets[ticket_id]
    # return {"deleted_ticket": ticket_id}
    #OR
    ticket = tickets.pop(ticket_id)
    return {"deleted_ticket": ticket}