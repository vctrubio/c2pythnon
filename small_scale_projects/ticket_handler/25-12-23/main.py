from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pony.orm import db_session
from typing import List
from pydantic import BaseModel
from models import *

app = FastAPI()

# Enable CORS for all origins (you might want to restrict this in a production environment)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to create a database session for each request
def get_db():
    with db_session:
        yield

class ApiTicket(BaseModel):
    name: str
    price: int
    category: Category
    quantity: int = 1
    paid: bool = False

class ApiUser(BaseModel):
    username: str
    tickets: List[ApiTicket] = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/{user_id}", response_model=ApiUser)
async def get_user(user_id: int, db: db_session = Depends(get_db)):
    user = Who.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    tickets = [{"name": ticket.name, "price": ticket.price, "quantity": ticket.quantity, "category": ticket.category} for ticket in user.tickets]
    return {"username": user.username, "tickets": tickets}

if __name__ == '__main__':
    connect_to_db()
    add_ticket_to_db(price=1113, name="fannyboys")
    # app.include_router(api_router, prefix="/api/v1")
