from typing import Required, Set
from pony.orm import *


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

if __name__ == '__main__':

    try:
        db.bind(provider='postgres', user='client', password='password', host='localhost', database='tickets_python')
        db.generate_mapping(create_tables=True)

        # Try to perform a database operation
        with db_session:
            User.select()[:1]
        print("Database connection successful.")
    except Exception as e:
        print(f"Database connection failed: {e}")

    print('Hello')


''' PONY DOC
Relationships in Pony are always defined by two attributes which represent both sides of a relationship.
many-to-many relationship between two entities, we should declare two Set attributes at both ends. 

'''