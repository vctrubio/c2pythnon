from typing import Optional
from enum import Enum
from sqlmodel import Field, SQLModel, create_engine, Session

DATABASE_URL = "postgresql://client:password@localhost:5432/tickets_python"
# psql -U client -d tickets_python -p 5431

class Category(Enum):
    A = 1 #Jardeniria
    B = 2 #Gasolina
    C = 3 #Vivienda
    D = 4 #Other

class Ticket(SQLModel, table=True):
    # id: Optional[int] = Field(default=None, primary_key=True)
    id: int = Field(primary_key=True)
    name: str #= Field(nullable=False)
    price: float #= Field(nullable=False)
    paid: bool = Field(default=False)
    category: Category = Field(default=Category.D)
    quantity: int = Field(default=1)

engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def add(*args):
    with Session(engine) as session:
        for i in args:
            session.add(i)
            session.commit()
            print(i, ' :commited')
    

def main():
    t_one = Ticket(name='Oliva', price=22)
    t_two = Ticket(name='Pan', price=4)
    add(t_one, t_two)
