from sqlalchemy.orm import Session
from . import models, schemas

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**dict(client))
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client_by_email(db: Session, email: str):
    return db.query(models.Participant).filter(models.Participant.email == email).first()
