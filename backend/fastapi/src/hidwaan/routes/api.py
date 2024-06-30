import jwt
from aiosqlite import Connection
from fastapi import APIRouter, Depends, HTTPException, Response, status

from .. import errors, service
from ..database import get_db
from ..dependency import get_current_user_raise
from ..models import Server, ServerCreate, User, UserCredential

router = APIRouter(
    prefix="/api/v1",
    tags=["v1"],
)


@router.post("/auth/user")
async def user_auth(
    credential: UserCredential, response: Response, db: Connection = Depends(get_db)
) -> User:
    user = await service.auth_user(db, credential.username, credential.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials."
        )
    token = jwt.encode(
        {"id": user.id, "username": user.username}, "secret", algorithm="HS256"
    )
    response.set_cookie(key="token", value=token)
    return user


@router.post("/auth/register")
async def user_register(
    credential: UserCredential, db: Connection = Depends(get_db)
) -> User:
    try:
        user = await service.create_user(db, credential.username, credential.password)
    except errors.UserExists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists."
        )
    except errors.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Failed to register. Please try again.",
        )
    return user


@router.get("/me")
async def me(current_user: User = Depends(get_current_user_raise)) -> User:
    return current_user


@router.get("/servers")
async def list_servers(db: Connection = Depends(get_db)) -> list[Server]:
    return await service.get_servers(db)


@router.post("/servers")
async def create_server(
    server_create: ServerCreate,
    db: Connection = Depends(get_db),
    current_user: User = Depends(get_current_user_raise),
) -> Server:
    server = await service.create_server(
        db,
        name=server_create.name,
        description=server_create.description,
        owner_id=current_user.id,
    )
    return server
