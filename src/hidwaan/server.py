from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from . import config

app = FastAPI()


templates = Jinja2Templates(directory=config.TEMPLATE_DIR)
app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")


class Server(BaseModel):
    id: int
    name: str
    description: str


server_list = [
    Server(**{"id": 1, "name": "Test", "description": "lorem ipsum"}),
    Server(**{"id": 2, "name": "Hello World", "description": "enjoy the chat!"}),
]


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/servers")
async def servers() -> list[Server]:
    return server_list


@app.post("/servers")
async def create_server(server: Server):
    return server_list


@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        print(data)
        await websocket.send_text(
            f'<div id="messages" hx-swap-oob="beforeend">{data['chat_message']}</div>'
        )
