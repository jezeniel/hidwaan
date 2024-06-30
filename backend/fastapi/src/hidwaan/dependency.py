from typing import Optional

import jwt
from fastapi import HTTPException, Request, status

from .models import User


def get_current_user(request: Request) -> Optional[User]:
    token = request.cookies.get("token")
    if not token:
        return None
    data = jwt.decode(token, "secret", algorithms=["HS256"])
    return User(id=data["id"], username=data["username"])


def get_current_user_raise(request: Request) -> User:
    user = get_current_user(request)
    if not user:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Not authorized.")
    return user
