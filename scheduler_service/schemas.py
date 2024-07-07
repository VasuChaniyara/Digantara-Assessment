from pydantic import BaseModel
from datetime import datetime

class JobBase(BaseModel):
    name: str
    interval: str
    details: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    last_run: datetime
    next_run: datetime

    class Config:
        orm_mode = True
