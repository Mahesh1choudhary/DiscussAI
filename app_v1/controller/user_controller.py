from fastapi import APIRouter, Body
from requests import Response, Request
from typing import Annotated

from app_v1.service.user_service import UserCreationRequest, Userservice

user_router = APIRouter()


class UserController():
    def __init__(self):
        user_service = Userservice()

    @user_router.post("/user")
    def create_user(user_creation_request = Annotated[UserCreationRequest, Body()]):
        try:

        except Exception as e:




