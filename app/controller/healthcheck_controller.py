from fastapi import APIRouter

healthcheck_router = APIRouter()

@healthcheck_router.get("/healthcheck")
async def get_healthcheck():
    return {"status": "ok"}
