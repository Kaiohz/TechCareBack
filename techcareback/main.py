from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from techcareback.sec.auth import get_api_key
from techcareback.util.config import Config
from techcareback.health.router import health_router
from techcareback.library.router import supplier_router
from techcareback.postgres.service import PostgresService

app = FastAPI(title="TechCare API")
BASE_PATH = "/rest/v1/{}"
Config = Config()
posstgres_service = PostgresService()

app.include_router(health_router)
app.include_router(supplier_router, prefix=BASE_PATH.format("library"),dependencies=[Depends(get_api_key)])

app.add_middleware(
    CORSMiddleware, 
    allow_origins=Config.ALLOWED_ORIGINS, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

@app.on_event("startup")
async def on_startup():
    await posstgres_service.create_db_and_tables()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
