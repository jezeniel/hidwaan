from pydantic import BaseModel


class ServerBase(BaseModel):
    name: str
    description: str


class Server(ServerBase):
    id: int
    name: str
    description: str


class ServerCreate(ServerBase):
    pass
