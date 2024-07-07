from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime
from scheduler import add_job_to_scheduler, remove_job_from_scheduler

def get_jobs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Job).offset(skip).limit(limit).all()

def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(
        name=job.name, 
        interval=job.interval, 
        details=job.details, 
        last_run=datetime.utcnow(), 
        next_run=datetime.utcnow()
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    add_job_to_scheduler(db_job.id, db_job.interval)
    return db_job

def delete_job(db: Session, job_id: int):
    db_job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if db_job:
        remove_job_from_scheduler(job_id)
        db.delete(db_job)
        db.commit()
    return db_job

