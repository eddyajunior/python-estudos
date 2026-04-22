from fastapi import Depends

from app.repositories.user_repository_contract import UserRepositoryContract
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

_user_repository = UserRepository()


def get_user_repository() -> UserRepositoryContract:
    return _user_repository


def get_user_service(
    user_repository: UserRepositoryContract = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repository)
