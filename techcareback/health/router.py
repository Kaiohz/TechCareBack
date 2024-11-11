from fastapi import APIRouter, Response

health_router = APIRouter()

@health_router.get("/health")
def read_health():
    return {"status": "healthy"}