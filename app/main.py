import asyncio
import threading

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from api.api_router import api_router
from infrastructure.redis_subscriber import set_loop, start_listener

origins = [
    "http://localhost:5173",
    "ws://localhost:5173",
]

@asynccontextmanager
async def lifespan(app: FastAPI):

    loop = asyncio.get_running_loop()
    set_loop(loop)

    thread = threading.Thread(target=start_listener, daemon=True)
    thread.start()

    print("Listener started")

    yield

app = FastAPI(title="Baqylau API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
