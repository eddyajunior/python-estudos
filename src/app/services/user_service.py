from app.models.user import UserCreate, UserResponse
from app.repositories.user_repository import UserRepository

class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: UserCreate) -> dict:
        created_user = self.user_repository.add(user)

        return {
            "message": "User created successfully",
            "data": created_user
        }
    
    def list_users(self) -> list[UserResponse]:
        return self.user_repository.list_all()