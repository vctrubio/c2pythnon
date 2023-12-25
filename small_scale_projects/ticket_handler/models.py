from typing import Required, Set
from pony.orm import *
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

db = Database()
class User(db.Entity):
    username = Required(str, unique=True)
    tickets = Set('Ticket')

class Ticket(db.Entity):
    price = Required(int)
    name = Required(str)
    paid = Optional(bool, default=False)
    user = Required(User)
    # quantity category

@db_session
def print_ticket_name(id):
    p = Ticket[id]
    print(p.name)

@db_session
def print_all_user():
    for u in User.select():
        print(u.username)

@db_session
def print_all_ticket():
    for u in Ticket.select():
        print(u.user.username, u.name)
    
if __name__ == '__main__':
    try:
        db.bind(provider='postgres', user='client', password='password', host='localhost', database='tickets_python')
        db.generate_mapping(create_tables=True)
        # Try to perform a database operation
        with db_session:
            me = User.select()[:1]
            me = me[0]
            print(me.username)
            # i = select(p for p in Ticket if p.price > 8)
            # for p in i:
            #     print(p.name)
        print("Database connection successful.")
    except Exception as e:
        print(f"Database connection failed: {e}")



''' PONY DOC
Relationships in Pony are always defined by two attributes which represent both sides of a relationship.
many-to-many relationship between two entities, we should declare two Set attributes at both ends. 

Even if a function just reads data and does not make any changes, it should use the db_session() in order to return the connection to the connection pool.
'''

''' SQL JOINS
select * from Ticket join "user" on Ticket.user = "user".id where "user".id = 1;
'''