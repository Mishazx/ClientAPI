from pydantic import BaseModel, EmailStr

class ClientCreate(BaseModel):
    avatar: str
    gender: str
    first_name: str
    last_name: str
    email: EmailStr

class Client(ClientCreate):
    id: int

    class Config:
        orm_mode = True
