CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    joined_at TEXT NOT NULL
);

CREATE INDEX idx_user_username ON user (username);
CREATE INDEX idx_user_joined_at ON user (joined_at);


CREATE TABLE server (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TEXT NOT NULL,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES user(id)
);

CREATE INDEX idx_server_name ON server (name);
CREATE INDEX idx_server_created_at ON server (created_at);


CREATE TABLE channel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    topic TEXT,
    server_id INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (server_id) REFERENCES server(id)
);

CREATE INDEX idx_channel_name ON channel (name);
CREATE INDEX idx_channel_created_at ON channel (created_at);


CREATE TABLE message (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    body TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE INDEX idx_message_username ON message (username);
CREATE INDEX idx_message_created_at ON message (created_at);
