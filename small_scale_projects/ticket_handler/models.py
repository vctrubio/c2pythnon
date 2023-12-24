

class User:
    username: str
    #has many tickets

class Ticket:
    price: int
    name: str
    paid: bool
    user: User #Has on user