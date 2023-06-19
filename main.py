from fastapi import FastAPI
from router.rt_auth import r_auth
from router.rt_users import r_users
from router.rt_portfolio import r_portfolio

app = FastAPI(title="REST API Portfolio", description="This is my portfolio", version="1.0.0", docs_url="/", redoc_url="/redocs", openapi_url="/openapi.json")

app.include_router(r_auth)
app.include_router(r_users)
app.include_router(r_portfolio)