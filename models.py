from sqlalchemy import Column, Integer, String, Text, Boolean, Date
from database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    details = Column(Text, nullable=False)
    banner_url = Column(String(255), nullable=False)
    is_featured = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)