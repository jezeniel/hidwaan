from typing import Optional

from aiosqlite import Connection

from .models import User


async def auth_user(db: Connection, username: str, password: str) -> Optional[User]:
    cur = await db.execute(
        "SELECT * FROM user WHERE username = ? AND password = ?",
        (username, password),
    )
    u = await cur.fetchone()
    if not u:
        return None
    return User(id=u["id"], username=u["username"])
