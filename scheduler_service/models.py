from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_run = Column(DateTime, default=datetime.utcnow)
    next_run = Column(DateTime, default=datetime.utcnow)
    interval = Column(String)  # (e.g., "daily", "weekly")
    details = Column(String)
