from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from .. import config

router = APIRouter(
    prefix="",
    tags=["web"],
)

templates = Jinja2Templates(directory=config.TEMPLATE_DIR)


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@router.get("/chat")
async def chatroom(request: Request):
    return templates.TemplateResponse(request=request, name="chat.html")
