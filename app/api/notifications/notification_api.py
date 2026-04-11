from fastapi import APIRouter
from infrastructure.tasks import send_notification

router = APIRouter()

@router.post("/notify")
def notify(message: str):
    send_notification.delay(message)
    return {"status": "queued"}
