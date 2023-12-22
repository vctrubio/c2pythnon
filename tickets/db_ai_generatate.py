from typing import Optional
from enum import Enum
from sqlmodel import Field, SQLModel, create_engine, Session
import os

DATABASE_URL = "postgresql://client:password@localhost:5432/tickets_python"
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)


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

def exit_program():
    print("Exiting the program.")

def clear_screen():
    os.system('clear')

def main_loop():
    options = {
        "1": {"text": "Add Ticket", "function": add_ticket},
        "2": {"text": "Update Ticket Price", "function": update_ticket_price},
        "3": {"text": "Delete Ticket", "function": delete_ticket},
        "4": {"text": "Print All Tickets", "function": print_all_tickets},
        "5": {"text": "Exit", "function": exit_program},
        "6": {"text": "Clear", "ptr": clear_screen},

    }

    while True:
        with Session(bind=engine) as session:  # Explicitly bind to the engine
            print("\nOptions:")
            for key, value in options.items():
                print(f"{key}. {value['text']}")

            choice = input(f"Enter your choice (1-{len(options)}): ")
            if choice in options:
                if choice == "1":
                    name = input("Enter ticket name: ")
                    price = float(input("Enter ticket price: "))
                    options[choice]["function"](session, name, price)
                elif choice in ["2", "3"]:
                    ticket_id = int(input("Enter ticket ID: "))
                    if choice == "2":
                        new_price = float(input("Enter new price: "))
                        options[choice]["function"](session, ticket_id, new_price)
                    else:
                        options[choice]["function"](session, ticket_id)
                elif choice == "4":
                    options[choice]["function"](engine, session)
                elif choice == "5":
                    print("Exiting the program.")
                    break
                elif choice == "6":
                    options[choice]['ptr']()
                    
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
