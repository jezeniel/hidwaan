import sqlite3

from hidwaan import config

con = sqlite3.connect(config.DB_FILE)
cur = con.cursor()

with open(config.ROOT_DIR / "db/000_create_tables.sql") as fp:
    cur.executescript(fp.read())
