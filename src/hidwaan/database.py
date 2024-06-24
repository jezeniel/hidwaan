import aiosqlite

from . import config


async def get_db():
    db = await aiosqlite.connect(config.DB_FILE)
    db.row_factory = aiosqlite.Row
    try:
        yield db
    finally:
        await db.close()
