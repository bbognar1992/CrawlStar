from fastapi import APIRouter, HTTPException
from app.celery_worker import crawl_website

router = APIRouter()

@router.post("/start_crawl")
async def start_crawl(crawler_name: str):
    crawl_website.apply_async(args=[crawler_name])
    return {"message": f"{crawler_name} started"}