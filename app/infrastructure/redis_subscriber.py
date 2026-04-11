import redis
import asyncio
from infrastructure.websocket_manager import manager

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

pubsub = r.pubsub()
pubsub.subscribe("notifications")

# 👇 сохраняем loop FastAPI
loop = None

def set_loop(app_loop):
    global loop
    loop = app_loop

def start_listener():
    for message in pubsub.listen():
        print("REDIS:", message)

        if message["type"] == "message":
            text = message["data"]

            asyncio.run_coroutine_threadsafe(
                manager.send_message(text),
                loop
            )
