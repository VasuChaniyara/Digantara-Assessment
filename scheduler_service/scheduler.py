from apscheduler.schedulers.background import BackgroundScheduler
from jobs import job_function

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.start()

def add_job_to_scheduler(job_id: int, interval: str):
    if interval == "daily":
        scheduler.add_job(job_function, 'interval', days=1, id=str(job_id))
    elif interval == "weekly":
        scheduler.add_job(job_function, 'interval', weeks=1, id=str(job_id))
    # Add more intervals as needed

def remove_job_from_scheduler(job_id: int):
    scheduler.remove_job(str(job_id))
