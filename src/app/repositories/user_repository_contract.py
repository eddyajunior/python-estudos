from typing import Protocol

from app.models.user import UserCreate, UserResponse

class UserRepositoryContract(Protocol):
    def add(self, user: UserCreate) -> UserResponse:
        ...

    def list_all(self) -> list[UserResponse]:
        ...