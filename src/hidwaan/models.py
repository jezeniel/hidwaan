from pydantic import BaseModel


class ServerBase(BaseModel):
    name: str
    description: str


class ServerCreate(ServerBase):
    pass


class Server(ServerBase):
    id: int


class ChannelBase(BaseModel):
    name: str


class Channel(ChannelBase):
    id: int


class ChannelCreate(ChannelBase):
    pass


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: int


class UserCredential(BaseModel):
    username: str
    password: str
