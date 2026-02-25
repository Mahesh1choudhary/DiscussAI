from fastapi import APIRouter, Body, Response, HTTPException
from typing import Annotated

from app_v1.commons.service_logger import setup_logger
from app_v1.service.user_service import UserCreationRequest, UserService

user_router = APIRouter()
logger = setup_logger()

user_service = UserService()

@user_router.post("/user", status_code=201)
def create_user(user_creation_request = Annotated[UserCreationRequest, Body()]):
    try:
        user_service.create_new_user(user_creation_request)
    except Exception as e:
        # TODO proper error handling
        logger.error(f"Error in new user creation : {e}")
        return HTTPException(status_code=500, detail=f"Internal Server Error")




