from fastapi import FastAPI, Depends
from app.routers import crawler, schedule
from app.celery_worker import celery_app
import uvicorn

app = FastAPI()

# Include routers
app.include_router(crawler.router)
app.include_router(schedule.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the web crawler admin panel!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
