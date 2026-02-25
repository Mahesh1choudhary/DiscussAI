from pydantic import BaseModel, Field

from app_v1.repository.user_repository import UserRepository

class UserCreationRequest(BaseModel):
    user_name:str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_]+$")
    email:str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_]+$")




class UserService():
    def __init__(self):
        self.user_repository = UserRepository()



    def create_new_user(self, user_creation_request: UserCreationRequest):
         = self.user_repository.find_by_user_name()
