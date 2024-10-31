from fastapi import APIRouter, HTTPException
from app.models import Schedule
from pydantic import BaseModel
from datetime import datetime

class ScheduleSchema(BaseModel):
    crawler_name: str
    run_at: datetime

router = APIRouter()

@router.post("/schedule_crawl")
async def schedule_crawl(schedule: ScheduleSchema):
    new_schedule = Schedule(**schedule.dict())
    return {"message": "Crawl scheduled"}