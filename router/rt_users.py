from fastapi import APIRouter, Depends, status
from dto.dt_users import InputUsers
from dto.dt_users import InputLogin
from dto.dt_base import ResponseWithData, ResponseStandard, OutputAuth, TokenData
from typing import Optional,List,Annotated
from service.sr_base import get_current_user
from models.enum_category import Category
from fastapi.security import OAuth2PasswordRequestForm


from service.sr_users import ServiceUsers

r_users = APIRouter(prefix="/api/v1", tags=["Users"], dependencies=[Depends(get_current_user)])

@r_users.post("/users", response_model=ResponseStandard)
def insert_new_users(
    # current_user: Annotated[TokenData, Depends(get_current_user)],
    new_users: InputUsers,
    service_users: ServiceUsers = Depends()
    ):
    result = service_users.insert(new_users)
    if result is None:
        return ResponseStandard(Status=False, Code=status.HTTP_400_BAD_REQUEST, Message="Email already exists")
    else:
        return ResponseStandard(Status=True, Code=status.HTTP_200_OK, Message="Data inserted successfully")