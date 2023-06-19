from fastapi import APIRouter, Depends, status
from dto.dt_users import InputLogin
from dto.dt_base import ResponseWithData, OutputAuth
from service.sr_base import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from service.sr_auth import ServiceAuth

r_auth = APIRouter(prefix="/api", tags=["Auth"])

# # Using Body request to get data from request body
# @r_auth.post("/auth", response_model=ResponseWithData)
# def login_users(input_login: InputLogin, service_auth: ServiceAuth = Depends()):
#     result = service_auth.login_user(input_login)
#     if result is None:
#         return ResponseWithData(Status=False, Code=status.HTTP_400_BAD_REQUEST, Message="Invalid email or password", Data=[])
#     else:
#         return ResponseWithData(Status=True, Code=status.HTTP_200_OK, Message="Login successfully", Data=OutputAuth(access_token=result, token_type="bearer").dict())

# Using OAuth2PasswordRequestForm to get data from request body
@r_auth.post("/auth", response_model=ResponseWithData)
def login_users(form_data: OAuth2PasswordRequestForm = Depends(), service_auth: ServiceAuth = Depends()):
    result = service_auth.login_user(InputLogin(email=form_data.username, password=form_data.password))
    if result is None:
        return ResponseWithData(Status=False, Code=status.HTTP_400_BAD_REQUEST, Message="Invalid email or password", Data=[])
    else:
        return ResponseWithData(Status=True, Code=status.HTTP_200_OK, Message="Login successfully", Data=OutputAuth(access_token=result, token_type="bearer").dict())
