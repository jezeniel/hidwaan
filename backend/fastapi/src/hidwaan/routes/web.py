from typing import Optional

from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .. import config
from ..dependency import get_current_user
from ..models import User

router = APIRouter(
    prefix="",
    tags=["web"],
)

templates = Jinja2Templates(directory=config.TEMPLATE_DIR)


@router.get("/")
async def index(
    request: Request, current_user: Optional[User] = Depends(get_current_user)
):
    if not current_user:
        return RedirectResponse("/login")
    return templates.TemplateResponse(
        request=request, name="index.html", context={"user": current_user}
    )


@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@router.get("/logout")
async def logout():
    response = RedirectResponse("/login")
    response.delete_cookie(key="token")
    return response


@router.get("/chat")
async def chatroom(request: Request):
    return templates.TemplateResponse(request=request, name="chat.html")
