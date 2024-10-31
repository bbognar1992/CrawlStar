# Web Crawler Application

This is a web crawler application built with **FastAPI**, **Celery**, **Dash**, and **Scrapy**. It allows scheduling multiple web crawlers, viewing crawl results, and managing schedules via an admin dashboard.

## Features

- **FastAPI** as the backend server for API requests.
- **Celery** to manage scheduled and background tasks.
- **Scrapy** for building customizable web crawlers.
- **Dash** to provide a user-friendly web-based admin panel.
- **SQLite** database for storing crawler schedules.

## Project Structure

```plaintext
web_crawler_app/
├── app/
│   ├── main.py               # FastAPI entry point
│   ├── celery_worker.py       # Celery configuration
│   ├── dash_app.py            # Dash app for scheduling and managing crawlers
│   ├── models.py              # SQLAlchemy models for scheduling
│   ├── routers/
│   │   ├── crawler.py         # API endpoints for crawler management
│   │   ├── schedule.py        # API endpoints for scheduling
├── crawlers/
│   ├── crawler_1/
│   │   ├── crawler.py         # Scrapy spider (crawler) example
├── data/                      # Persistent storage for SQLite database
├── requirements.txt           # Package dependencies
├── Dockerfile                 # Docker configuration
└── docker-compose.yml         # Docker Compose setup
```

## Getting Started

### Prerequisites

- **Docker** and **Docker Compose** installed on your machine.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/web_crawler_app.git
    cd web_crawler_app
    ```

2. Build and run the containers with Docker Compose:

    ```bash
    docker-compose up --build
    ```

This will start the following services:

- **FastAPI** on `http://localhost:8000`
- **Dash** on `http://localhost:8050`
- **Celery** worker for task scheduling
- **Redis** as the message broker for Celery

### Accessing the Services

- **FastAPI API**: Visit `http://localhost:8000/docs` to view the API documentation.
- **Dash Admin Panel**: Go to `http://localhost:8050` to manage and schedule crawlers.

## Using the Application

### Adding New Crawlers

1. **Create a Scrapy Spider**: Each new crawler should be created as a Scrapy spider in the `crawlers/` directory.
2. **Update the Celery Worker**: Register the new spider in `app/celery_worker.py` by adding it to the `crawl_website` function.

### Scheduling Crawlers

1. Open the **Dash Admin Panel** at `http://localhost:8050`.
2. Enter the crawler name and the desired date and time for the crawl.
3. Click "Schedule Crawl" to add the crawl to the queue.

The crawl schedule is stored in the SQLite database, and Celery will handle execution at the specified time.

### API Endpoints

- **Start Crawl**: `POST /start_crawl` - Start a crawl immediately for a specific crawler.
- **Schedule Crawl**: `POST /schedule_crawl` - Schedule a crawl for a specific date and time.

### Database

This application uses **SQLite** for simplicity. The database file `test.db` is located in the `data/` folder, and this directory is mounted as a Docker volume to ensure persistence.

## Configuration

- **Database**: The SQLite database is defined in `DATABASE_URL` within `models.py`.
- **Celery Broker**: Redis is used as the message broker for Celery, defined in `celery_worker.py`.

## Troubleshooting

- **Dash App Not Loading**: Ensure that both FastAPI and Dash services are running by checking the logs (`docker-compose logs fastapi` and `docker-compose logs dash`).
- **Database Issues**: If the `test.db` file is not being saved, verify that the `data/` folder is correctly mounted in `docker-compose.yml`.

## Future Enhancements

- **User Authentication**: Secure the admin panel with login functionality.
- **Crawler Status Tracking**: Display the status of each scheduled crawl (e.g., pending, in progress, completed).
- **Error Handling and Alerts**: Add notifications for failed crawls or scheduling issues.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.