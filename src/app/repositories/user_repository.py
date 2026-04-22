from app.models.user import UserCreate, UserResponse

class UserRepository:
    def __init__(self):
        self._users: list[UserResponse] = []
        self._next_id: int = 1


    def add(self, user: UserCreate) -> UserResponse:
        new_user = UserResponse(
            id=self._next_id,
            name=user.name,
            email=user.email,
            age=user.age
        )
        
        self._users.append(new_user)
        self._next_id += 1
        
        return new_user
    
    def list_all(self) -> list[UserResponse]:
        return self._users