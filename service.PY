from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from model import ShipmentModel

def create_shipment(db: Session, tracking_number: str):
    # Kiểm tra trùng lặp
    existing = db.query(ShipmentModel).filter(ShipmentModel.tracking_number == tracking_number).first()
    if existing:
        raise HTTPException(status_code=400, detail="Mã vận đơn này đã được khởi tạo trước đó")
    
    new_shipment = ShipmentModel(tracking_number=tracking_number)
    db.add(new_shipment)
    db.commit()
    db.refresh(new_shipment)
    return new_shipment

def get_all_shipments(db: Session):
    return db.query(ShipmentModel).all()