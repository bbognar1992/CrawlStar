from celery import Celery

# Configure Celery to use Redis as broker and backend
celery_app = Celery(
    "web_crawler",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

celery_app.conf.update(task_routes={
    "app.tasks.crawl_website": {"queue": "crawling"},
})

@celery_app.task
def crawl_website(crawler_name: str):
    from scrapy.crawler import CrawlerProcess
    from crawlers.crawler_1.crawler import Crawler1Spider

    process = CrawlerProcess()
    if crawler_name == "crawler_1":
        process.crawl(Crawler1Spider)
    process.start()