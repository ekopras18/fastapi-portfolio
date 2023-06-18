from fastapi import APIRouter, Depends, status
from dto.dt_users import InputUsers
from dto.dt_users import InputLogin
from dto.dt_base import ResponseWithData, ResponseStandard, OutputAuth
from typing import Optional,List
from models.enum_category import Category
# from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm


from service.sr_users import ServiceUsers

r_users = APIRouter(prefix="/api/v1", tags=["Users"])

@r_users.post("/users", response_model=ResponseStandard)
def insert_new_users(new_users: InputUsers, service_users: ServiceUsers = Depends()):
    result = service_users.insert(new_users)
    if result is None:
        return ResponseStandard(Status=False, Code=status.HTTP_400_BAD_REQUEST, Message="Email already exists")
    else:
        return ResponseStandard(Status=True, Code=status.HTTP_200_OK, Message="Data inserted successfully")
# Using Body request to get data from request body
@r_users.post("/login", response_model=ResponseWithData)
def login_users(input_login: InputLogin, service_users: ServiceUsers = Depends()):
    result = service_users.login_user(input_login)
    if result is None:
        return ResponseWithData(Status=False, Code=status.HTTP_400_BAD_REQUEST, Message="Invalid email or password", Data=[])
    else:
        return ResponseWithData(Status=True, Code=status.HTTP_200_OK, Message="Login successfully", Data=OutputAuth(access_token=result, token_type="bearer").dict())

# Using OAuth2PasswordRequestForm to get data from request body
# @r_users.post("/login", response_model=ResponseWithData)
# def login_users(form_data: OAuth2PasswordRequestForm = Depends(), service_users: ServiceUsers = Depends()):
#     result = service_users.login_user(InputLogin(email=form_data.username, password=form_data.password))
#     if result is None:
#         return ResponseWithData(Status=False, Code=status.HTTP_400_BAD_REQUEST, Message="Invalid email or password", Data=[])
#     else:
#         return ResponseWithData(Status=True, Code=status.HTTP_200_OK, Message="Login successfully", Data=OutputAuth(access_token=result, token_type="bearer").dict())
