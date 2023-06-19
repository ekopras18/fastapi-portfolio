from fastapi import APIRouter, Depends, status
from dto.dt_portfolio import InputPortfolio
from models.md_portfolio import Portfolio
from typing import Optional, List, Annotated
from models.enum_category import Category
from dto.dt_base import ResponseStandard, ResponseWithData, TokenData
from pydantic import parse_obj_as
from service.sr_base import get_current_user
from service.sr_portfolio import ServicePortfolio
from router.rt_base import convert_id_to_string

r_portfolio = APIRouter(prefix="/api/v1", tags=["Portfolio"], dependencies=[Depends(get_current_user)])


@r_portfolio.post("/portfolio", response_model=ResponseWithData)
def insert_new_portfolio(
    new_portfolio: InputPortfolio,
    # current_user: Annotated[TokenData, Depends(get_current_user)],
    service_portfolio: ServicePortfolio = Depends()
):
    service_portfolio.insert(new_portfolio)
    return ResponseStandard(Status=True, Code=status.HTTP_200_OK, Message="Data inserted successfully")

@r_portfolio.get("/portfolio", response_model=ResponseWithData)
def get_portfolio(
    # current_user: Annotated[TokenData, Depends(get_current_user)],
    category: Optional[Category] = None,
    service_portfolio: ServicePortfolio = Depends()
):
    result = service_portfolio.get(category)
    if len(result) == 0:
        return ResponseWithData(Status=False, Code=status.HTTP_400_BAD_REQUEST, Message="Data not found", Data=[])
    else:
        # convert id=ObjectId('xxxx') ke id='xxxx'
        result = convert_id_to_string(result)
        return ResponseWithData(Status=True, Code=status.HTTP_200_OK, Message="Data Found", Data=result)
