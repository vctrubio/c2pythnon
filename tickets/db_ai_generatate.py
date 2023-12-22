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

##################################GUI#####################################################
import tkinter as tk
from tkinter import messagebox

class TicketManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Manager")

        # Add Ticket Entry Widgets
        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Price:").grid(row=1, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=1, column=1)

        tk.Button(root, text="Add Ticket", command=self.add_ticket).grid(row=2, column=0, columnspan=2, pady=10)

        # Ticket Listbox
        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.grid(row=3, column=0, columnspan=2, pady=10)

        # Buttons for Update and Delete
        tk.Button(root, text="Update Price", command=self.update_ticket).grid(row=4, column=0, pady=5)
        tk.Button(root, text="Delete Ticket", command=self.delete_ticket).grid(row=4, column=1, pady=5)

        # Print All Tickets Button
        tk.Button(root, text="Print All Tickets", command=self.print_all_tickets).grid(row=5, column=0, columnspan=2, pady=10)

    def add_ticket(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        add_ticket(Session(bind=engine), name, price)
        self.update_listbox()

    def update_ticket(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            ticket_id = int(selected_index[0]) + 1  # Adjust the index for 1-based ID
            new_price = float(self.price_entry.get())
            update_ticket_price(Session(bind=engine), ticket_id, new_price)
            self.update_listbox()

    def delete_ticket(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            ticket_id = int(selected_index[0]) + 1  # Adjust the index for 1-based ID
            delete_ticket(Session(bind=engine), ticket_id)
            self.update_listbox()

    def print_all_tickets(self):
        print_all_tickets(engine, Session(bind=engine))
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        tickets = get_all_tickets(Session(bind=engine))
        for ticket in tickets:
            self.listbox.insert(tk.END, f"{ticket.id}: {ticket.name} - ${ticket.price}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TicketManagerApp(root)
#     root.mainloop()
