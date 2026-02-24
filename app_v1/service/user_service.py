from pydantic import BaseModel, Field

from app_v1.service.database_service import DatabaseService

class UserCreationRequest(BaseModel):
    user_name:str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_]+$")

class Userservice():
    def __init__(self):
        self.database_service = DatabaseService()



    def create_new_user(self,):
        pass