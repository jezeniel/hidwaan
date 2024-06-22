from fastapi import FastAPI, Request, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import config
from .models import Server, ServerCreate

app = FastAPI()


templates = Jinja2Templates(directory=config.TEMPLATE_DIR)
app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")


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
async def create_server(server: ServerCreate) -> Server:
    new_server = Server(
        id=len(server_list) + 1, name=server.name, description=server.description
    )
    server_list.append(new_server)
    return new_server


@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_text("")
