from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Boolean, Column, Integer, String

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓        ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
SQLALCHEMY_DATABASE_URL = "sqlite:///db_test_1.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SQLite  

# sessionmakersession
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
             #                
Base = declarative_base() #  ORM 

class M_User(Base):  #
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) # 
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String) 
    is_active = Column(Boolean, default=True)

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    class Config:
        orm_mode = True

Base.metadata.create_all(bind=engine) # 

app = FastAPI()

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓        ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
def get_db():
    try:
        db = SessionLocal() # ''
        yield db            # generator
    finally:
        db.close()
        print('')
    

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓        ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
# id
def get_user(db: Session, user_id: int):
    CCCCCC = db.query(M_User).filter(M_User.id == user_id).first()
    print('CCCCCC :', CCCCCC) # 
    return CCCCCC


if __name__ == "__main__":
    for i in get_db():
        c = get_user(db=i,user_id=2)
        print(c.email)
