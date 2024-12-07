from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import Event
from pydantic import BaseModel
import datetime

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Modelo para criar/atualizar eventos
class EventCreate(BaseModel):
    name: str
    date: datetime.datetime
    week_day: str
    details: str
    banner_url: str
    is_featured: bool = False
    is_active: bool = True

# Rota para criar evento
@app.post("/events/")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Event(
        name=event.name,
        date=event.date,
        week_day=event.week_day,
        details=event.details,
        banner_url=event.banner_url,
        is_featured=event.is_featured,
        is_active=event.is_active
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

# Rota para listar eventos
@app.get("/events/")
def list_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    return events

# Rota simples
@app.get("/")
def read_root():
    return {"message": "API is working!"}
