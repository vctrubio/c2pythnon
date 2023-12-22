from typing import Optional
from enum import Enum
from sqlmodel import Field, SQLModel, create_engine, Session

DATABASE_URL = "postgresql://client:password@localhost:5432/tickets_python"
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

class Category(Enum):
    A = 1  # Jardeniria
    B = 2  # Gasolina
    C = 3  # Vivienda
    D = 4  # Other


class Ticket(SQLModel, table=True):
    __table_args__ = {'extend_existing': True}
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False)
    price: float = Field(nullable=False)
    paid: bool = Field(default=False)
    category: Category = Field(default=Category.D)
    quantity: int = Field(default=1)

# ... (previous code)

def add_ticket(session: Session, name: str, price: float):
    ticket = Ticket(name=name, price=price)
    session.add(ticket)
    session.commit()
    print(f"Ticket added: {ticket}")

def update_ticket_price(session: Session, ticket_id: int, new_price: float):
    ticket = session.get(Ticket, ticket_id)
    if ticket:
        ticket.price = new_price
        session.commit()
        print(f"Ticket updated: {ticket}")

def delete_ticket(session: Session, ticket_id: int):
    ticket = session.get(Ticket, ticket_id)
    if ticket:
        session.delete(ticket)
        session.commit()
        print(f"Ticket deleted: {ticket}")

def get_all_tickets(session: Session):
    tickets = session.query(Ticket).all()
    return tickets

def print_all_tickets(engine: engine, session: Session):
    with Session(bind=engine) as session:  # Explicitly bind to the engine
        tickets = get_all_tickets(session)
        print("All Tickets:")
        for ticket in tickets:
            print(ticket)
