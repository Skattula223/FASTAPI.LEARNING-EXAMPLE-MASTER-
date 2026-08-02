# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta

import jwt
from fastapi import Depends, FastAPI, HTTPException # , status
from starlette import status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from passlib.context import CryptContext # passlib 
from pydantic import BaseModel



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# verify_password   plain_password      hashed_password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
# 
def get_password_hash(password):
    return pwd_context.hash(password)


if __name__ == "__main__":
    ########################################################
    xxx = get_password_hash('cccccc')
    yyy = get_password_hash('cccccc')
    print(xxx)
    print(yyy)
    print('verify_password',verify_password('cccccc',xxx))
    print('verify_password',verify_password('cccccc',yyy))
    print('verify_password',verify_password('secret','$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW'))



    ############################timedelta###########################
    from datetime import datetime
    from datetime import timedelta
    aDay = timedelta(minutes=30) # timedeltadatetimedatetime
    now = datetime.now() + aDay
    print(aDay)
    print(datetime.now())
    print(now ,type(now))
    
    