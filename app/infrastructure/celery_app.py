from celery import Celery

celery_app = Celery(
    "notifications",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
    include=["infrastructure.tasks"],
)
