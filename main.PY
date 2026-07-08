from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from service import create_shipment, get_all_shipments

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/shipments")
def add_shipment(tracking_number: str, db: Session = Depends(get_db)):
    return create_shipment(db, tracking_number)

@app.get("/shipments")
def get_shipments(db: Session = Depends(get_db)):
    return get_all_shipments(db)