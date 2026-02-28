from app_v1.models.request_models.user_creation_request import UserCreationRequest
from app_v1.database.database_models.user_model import User
from app_v1.repository.user_repository import UserRepository
from app_v1.database.database_manager import DatabaseManager


class UserService():
    def __init__(self, database_manager: DatabaseManager):
        self.database_manager = database_manager



    def create_new_user(self, user_creation_request: UserCreationRequest):

        with self.database_manager.transaction() as session:
            repo = UserRepository(session)
            already_existing_user:User = repo.find_by_user_name(user_creation_request.user_name)
            if already_existing_user:
                raise ValueError("Username already taken")
            new_user = User(user_name = user_creation_request.user_name, email = str(user_creation_request.email))
            repo.save_user(new_user)
            return new_user

