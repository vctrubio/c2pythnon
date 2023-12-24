from typing import List, Optional
from sqlmodel import SQLModel, Field, create_engine, Session


class User(SQLModel):
    username: str = Field(unique=True)
    # has many tickets


class Ticket(SQLModel):
    price: int
    name: str
    paid: bool = Field(default=False)
    user: User # has one user


class GroupTicket(SQLModel):
    tickets: List[Ticket] = []
    total_price: Optional[int] = None


if __name__ == '__main__':
    migel = User(username='migel')
    myticket = Ticket(name="11", price=11, user=migel)
    mygroup = GroupTicket()
    print(myticket)
    print(mygroup)
