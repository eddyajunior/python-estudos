from app.models.user import UserCreate, UserResponse


class UserRepository:
    def __init__(self) -> None:
        self._users: list[UserResponse] = []
        self._next_id: int = 1

    def add(self, user: UserCreate) -> UserResponse:
        new_user = UserResponse(
            id=self._next_id, name=user.name, email=user.email, age=user.age
        )

        self._users.append(new_user)
        self._next_id += 1

        return new_user

    def list_all(self) -> list[UserResponse]:
        return self._users

    def get_by_id(self, user_id: int) -> UserResponse | None:
        for user in self._users:
            if user.id == user_id:
                return user
        return None
    
    def delete(self, user_id: int) -> bool:
        for index, user in enumerate(self._users):
            if user.id == user_id:
                del self._users[index]
                return True
        return False
