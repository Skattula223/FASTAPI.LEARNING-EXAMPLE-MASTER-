from typing import List
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
# SELECT * FROM users 

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓        ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
SQLALCHEMY_DATABASE_URL = "sqlite:///db_test_3.db"
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

Base.metadata.create_all(bind=engine)

app = FastAPI()

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓        ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
def get_db():
    try:
        db = SessionLocal() # ''
        yield db            # 
    finally:
        db.close()
        print('')


"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓        ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
# id
def get_user(db: Session, user_id: int):
    CCCCCC = db.query(M_User).filter(M_User.id == user_id).first()
    print(CCCCCC)           # 
    return CCCCCC

# 
def db_create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = M_User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()     # 
    db.refresh(db_user) # 
    return db_user

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    postget    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
# (post)
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Depends(get_db)
    return db_create_user(db=db, user=user)

# ID
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    print(db_user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)