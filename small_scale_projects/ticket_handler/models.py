from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship, create_engine, Session


# has many tickets
class Ticket(SQLModel):
    price: int
    name: str
    paid: bool = Field(default=False)
    user: 'User' #= Relationship(back_populates="tickets")

    def user_id(self):
        return self.user.username

class User(SQLModel):
    username: str = Field(unique=True)
    tickets: List['Ticket'] = Relationship(back_populates="user")

    
class GroupTicket(SQLModel):
    tickets: List[Ticket] = []
    total_price: Optional[int] = None

'''
The back_populates parameter is used to set up a two-way relationship. 
This means that you can access the User of a Ticket through the user field, 
and you can access the Tickets of a User through the tickets field.
'''
Ticket.user = Relationship(back_populates="tickets")

if __name__ == '__main__':
    migel = User(username='migel')
    myticket = Ticket(name="11", price=11, user=migel)
    mygroup = GroupTicket()
    u = myticket.user
    # print(myticket.user_id())
    print(migel)

    # print(myticket.user_id())
    # print(mygroup)
