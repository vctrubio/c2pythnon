from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str
    is_income: bool

class TransactionModel(TransactionBase):
    id: int

    class Config:
        orm_mode = True


def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_depenency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return {'message': 'Hello World!'}


@app.post('/transactions/', response_model=TransactionModel)
async def create_transaction(transaction: TransactionBase, db: db_depenency):
    db_transaction = models.Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.get('/transactions/', response_model=List[TransactionModel])
async def read_transaction(db: db_depenency, skip: int = 0, limit: int = 100):
    return db.query(models.Transaction).offset(skip).limit(limit).all()


@app.delete('/transactions/{transaction_id}')
async def delete_transaction(transaction_id: int, db: db_depenency):
    db.query(models.Transaction).filter(models.Transaction.id == transaction_id).delete()
    db.commit()
    return {'message': 'Transaction deleted!'}