from models import Ticket, Div
import os
tickets = []
    
#first param is price, second param optional is div
def ticket_add():
    try:
        price = input("New Ticket Price: ")
        # div = input("New Ticket Division: ")
        # if div == ('' or 'E'):
        #     div = 'C'
        # div_enum = Div[div]
        # ticket = Ticket(price, div_enum)
        ticket = Ticket(price=int(price))
        tickets.append(ticket)
        print("Ticket added successfully")
    except Exception as e:
        print(f'{e}')

def ticket_all():
    for ticket in tickets:
        print(ticket)

def ticket_show():
    for e, ticket in enumerate(tickets):
        print(f"{e}: {ticket}")
    i = input("Select Ticket ID: ")
    try:
        print(tickets[int(i)])
    except Exception as e:
       print(f'{e}') 

def ticket_delete():
    for e, ticket in enumerate(tickets):
        print(f"{e}: {ticket}")
    i = input("Select Ticket ID: ")
    try:
        del tickets[int(i)]
    except Exception as e:
       print(f'{e}')

def ticket_update():
    if not tickets:
        print('tickets are empty')
        return 
    for e, ticket in enumerate(tickets):
        print(f"{e}: {ticket}")
    i = input("Select Ticket ID: ")
    try:
        price = input("New Ticket Price: ")
        tickets[int(i)].price = price
    except Exception as e:
       print(f'{e}')

def menu():
    print("--  press  --")
    print('a or "add"')
    print('e or "exit"')
    print('s or "show"')
    print('x or "all"')
    print('d or "delete"')
    print('u or "update"')
    print('c or "clear"')



def run():
    while True:
        menu()
        str = input('>')
        if str == ('e' or 'exit'):
            break
        elif str == ('a' or 'add'):
            ticket_add()
        elif str == ('s' or 'show'):
            ticket_show()
        elif str == ('x' or 'all'):
            ticket_all()
        elif str == ('c' or 'clear'):
            os.system('clear')
        elif str == ('d' or 'delete'):
            ticket_delete()
        elif str == ('u' or 'update'):
            ticket_update()
            