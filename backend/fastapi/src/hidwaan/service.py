from datetime import UTC, datetime
from typing import Optional

from aiosqlite import Connection, IntegrityError

from . import errors
from .models import Server, User


async def auth_user(db: Connection, username: str, password: str) -> Optional[User]:
    cur = await db.execute(
        "SELECT * FROM user WHERE username = ? AND password = ?",
        (username, password),
    )
    u = await cur.fetchone()
    if not u:
        return
    return User(id=u["id"], username=u["username"])


async def create_user(db: Connection, username: str, password: str) -> User:
    now = datetime.now(UTC).isoformat()

    try:
        cur = await db.execute(
            "INSERT INTO user (username, password, joined_at) VALUES (?, ?, ?)",
            (username, password, now),
        )
        await db.commit()
    except IntegrityError:
        raise errors.UserExists("User already exists")

    cur = await db.execute(
        "SELECT id, username FROM user WHERE id = ?", (cur.lastrowid,)
    )
    user = await cur.fetchone()
    if not user:
        raise errors.DoesNotExist("User does not exist")

    return User(id=user["id"], username=user["username"])


async def get_servers(db: Connection) -> list[Server]:
    cur = await db.execute("SELECT * FROM server")
    servers = await cur.fetchall()
    results = []
    for s in servers:
        results.append(Server(id=s["id"], name=s["name"], description=s["description"]))
    return results


async def create_server(
    db: Connection, name: str, description: str, owner_id: int
) -> Server:
    now = datetime.now(UTC).isoformat()
    cur = await db.execute(
        "INSERT INTO server (name, description, owner_id, created_at) VALUES (?, ?, ?, ?)",
        (name, description, owner_id, now),
    )
    await db.commit()
    cur = await db.execute("SELECT * FROM server WHERE id = ?", (cur.lastrowid,))
    server = await cur.fetchone()
    if not server:
        raise errors.DoesNotExist("Server does not exist")

    return Server(**server)
