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
    
    def get_by_id(self, user_id: int) -> UserResponse | None:
        if user_id == 999:
            return UserResponse(
                id=999,
                name="[FAKE] Edson",
                email="teste@teste.com",
                age=30
            )
        return None 
    
    def delete(self, user_id: int) -> bool:
        return user_id == 999