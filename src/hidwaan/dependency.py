import jwt
from fastapi import HTTPException, Request, status

from .models import User


def get_current_user(request: Request) -> User:
    token = request.cookies.get("token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authenticated"
        )
    data = jwt.decode(token, "secret", algorithms=["HS256"])
    return User(id=data["id"], username=data["username"])
