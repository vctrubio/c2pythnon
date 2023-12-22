from dataclasses import dataclass, field
from enum import Enum

class Div(Enum):
    A = 1 #Jardeniria
    B = 2 #Gasolina
    C = 3 #Vivienda
    D = 4 #Unspecified

@dataclass
class Ticket:
    id: int = 1
    price: float = field(default=21)
    div: Div = field(default=Div.D)
    quantity: int = 1

    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.quantity < 1:
            raise ValueError("Quantity must be at least 1")
        if not isinstance(self.div, Div):
            raise ValueError("Div must be an instance of the Div enum")
   