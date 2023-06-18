from fastapi import APIRouter, Depends, status
from dto.dt_portfolio import InputPortfolio
from models.md_portfolio import Portfolio
from typing import Optional, List
from models.enum_category import Category
from dto.dt_base import ResponseStandard, ResponseWithData
from pydantic import parse_obj_as




from service.sr_portfolio import ServicePortfolio

r_portfolio = APIRouter(prefix="/api/v1", tags=["Portfolio"])


@r_portfolio.post("/portfolio")
def insert_new_portfolio(
    new_portfolio: InputPortfolio, service_portfolio: ServicePortfolio = Depends()
):
    service_portfolio.insert(new_portfolio)
    return ResponseStandard(Status=True, Code=status.HTTP_200_OK, Message="Data inserted successfully")

@r_portfolio.get("/portfolio")
def get_portfolio(
    category: Optional[Category] = None, service_portfolio: ServicePortfolio = Depends()
):
    result = service_portfolio.get(category)
    if len(result) == 0:
        return {"Status": False, "Code": 404, "Message": "Data not found", "Data": []}
    else:
        # convert id=ObjectId('xxxx') ke id='xxxx'
        converted_data_list = []
        for item in result:
            converted_item = item.copy()
            converted_item.id = str(item.id)
            converted_data_list.append(converted_item)
        
        return ResponseWithData(Status=True, Code=status.HTTP_200_OK, Message="Data Found", Data=converted_data_list)
