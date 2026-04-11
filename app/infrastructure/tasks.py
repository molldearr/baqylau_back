from infrastructure.celery_app import celery_app
import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

@celery_app.task
def send_notification(message: str):
    print("CELERY TASK:", message)

    # 🔥 отправляем в Redis канал
    r.publish("notifications", message)
