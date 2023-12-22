from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import create_engine, Session
from controller import Ticket, add_ticket, delete_ticket, print_all_tickets, engine


app = FastAPI()

@app.post("/tickets", response_model=dict)
def add_ticket_route(ticket: Ticket):
    add_ticket(Session(bind=engine), ticket.name, ticket.price)
    return {"message": "Ticket added successfully"}

@app.get("/tickets", response_model=list[dict])
def get_all_tickets_route():
    with Session(bind=engine) as session:
        tickets = print_all_tickets(session)
        return [{"id": ticket.id, "name": ticket.name, "price": ticket.price} for ticket in tickets]

@app.delete("/tickets/{ticket_id}", response_model=dict)
def delete_ticket_route(ticket_id: int):
    with Session(bind=engine) as session:
        deleted_ticket = delete_ticket(session, ticket_id)
        if deleted_ticket:
            return {"message": f"Ticket with ID {ticket_id} deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail=f"Ticket with ID {ticket_id} not found")

