from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app_v1.repository.user_repository import UserRepository
from app_v1.service.user_service import UserService
from app_v1.database.database_manager import DatabaseManager


def get_user_service():
    database_manager = DatabaseManager()
    return UserService(database_manager)

