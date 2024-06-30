from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles

from . import config
from .routes import api, web

app = FastAPI()
app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")
app.include_router(web.router)
app.include_router(api.router)


connected = set()


@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected.add(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            for conn in connected:
                await conn.send_json(data)
    except WebSocketDisconnect:
        connected.remove(websocket)
