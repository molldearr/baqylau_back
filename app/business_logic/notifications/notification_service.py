from infrastructure.redis_client import redis_client


class NotificationService:
    def send_notification(self, message: str):
        redis_client.publish("notifications", message)
        
        print("Жіберілді: ", message)
        
        return {"status": "sent", "message": message}
