from app.models.user import UserCreate, UserResponse
from app.repositories.user_repository_contract import UserRepositoryContract


class UserService:
    def __init__(self, user_repository: UserRepositoryContract) -> None:
        self.user_repository = user_repository

    def create_user(self, user: UserCreate) -> dict:
        created_user = self.user_repository.add(user)

        return {
            "message": "Usuário criado com sucesso",
            "data": created_user
        }

    def list_users(self) -> list[UserResponse]:
        return self.user_repository.list_all()
    
    def get_user_by_id(self, user_id: int) -> UserResponse | None:
        return self.user_repository.get_by_id(user_id)