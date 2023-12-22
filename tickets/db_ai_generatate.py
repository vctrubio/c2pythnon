from typing import Optional
from enum import Enum
from sqlmodel import Field, SQLModel, create_engine, Session

DATABASE_URL = "postgresql://client:password@localhost:5431/tickets_python"

class Category(Enum):
    A = 1  # Jardeniria
    B = 2  # Gasolina
    C = 3  # Vivienda
    D = 4  # Other

class Ticket(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False)
    price: float = Field(nullable=False)
    paid: bool = Field(default=False)
    category: Category = Field(default=Category.D)
    quantity: int = Field(default=1)

engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def add_ticket(name: str, price: float):
    ticket = Ticket(name=name, price=price)
    with Session() as session:
        session.add(ticket)
        session.commit()
        print(f"Ticket added: {ticket}")

def update_ticket_price(ticket_id: int, new_price: float):
    with Session() as session:
        ticket = session.get(Ticket, ticket_id)
        if ticket:
            ticket.price = new_price
            session.commit()
            print(f"Ticket updated: {ticket}")

def delete_ticket(ticket_id: int):
    with Session() as session:
        ticket = session.get(Ticket, ticket_id)
        if ticket:
            session.delete(ticket)
            session.commit()
            print(f"Ticket deleted: {ticket}")

def get_all_tickets():
    with Session() as session:
        tickets = session.query(Ticket).all()
        return tickets

def print_all_tickets():
    tickets = get_all_tickets()
    print("All Tickets:")
    for ticket in tickets:
        print(ticket)

def main_loop():
    while True:
        print("\nOptions:")
        print("1. Add Ticket")
        print("2. Update Ticket Price")
        print("3. Delete Ticket")
        print("4. Print All Tickets")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter ticket name: ")
            price = float(input("Enter ticket price: "))
            add_ticket(name, price)
        elif choice == "2":
            ticket_id = int(input("Enter ticket ID: "))
            new_price = float(input("Enter new price: "))
            update_ticket_price(ticket_id, new_price)
        elif choice == "3":
            ticket_id = int(input("Enter ticket ID: "))
            delete_ticket(ticket_id)
        elif choice == "4":
            print_all_tickets()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

