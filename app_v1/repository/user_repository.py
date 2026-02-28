from sqlalchemy.orm import Session
from typing import Optional

from app_v1.database.database_models.user_model import User

class UserRepository():
    def __init__(self, database_session: Session):
        self.database_session = database_session

    def find_by_user_name(self, user_name:str):
        user:Optional[User] = self.database_session.query(User).filter(User.user_name == user_name).first()
        return user

    def save_user(self, user:User):
        self.database_session.add(user)