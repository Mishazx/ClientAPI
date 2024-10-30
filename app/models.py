from sqlalchemy import Column, Integer, String
from database import Base

class Client(Base):
    __tablename__ = "Client"
    
    id = Column(Integer, primary_key=True, index=True)
    avatar = Column(String, index=True)
    gender = Column(String, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
