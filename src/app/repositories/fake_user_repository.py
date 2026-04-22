from app.models.user import UserCreate, UserResponse


class FakeUserRepository:
    def add(self, user: UserCreate) -> UserResponse:
        return UserResponse(
            id=999,
            name=f"[FAKE] {user.name}",
            email=user.email,
            age=user.age
        )

    def list_all(self) -> list[UserResponse]:
        return [
            UserResponse(
                id=999,
                name="[FAKE] Edson",
                email="edson@email.com",
                age=30
            )
        ]