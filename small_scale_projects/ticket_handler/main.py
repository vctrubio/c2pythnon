from models import *
from tutorial_fastapi import *


@db_session
def tr():
    me = Ticket(price=10, name="ticketf120033", user=1, category=Category.JARDIN.value, quantity=1)
    print('ticket added', me.name)

if __name__ == '__main__':
    # add_user_to_db()
    # tr()
    print_all_ticket()