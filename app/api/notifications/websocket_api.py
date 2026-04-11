from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from infrastructure.websocket_manager import manager

router = APIRouter()

@router.websocket("/notifications")
async def ws(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
