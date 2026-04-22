from fastapi import APIRouter, Depends

from app.models.user import UserCreate
from app.services.user_service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["users"])


def get_user_service() -> UserService:
    return UserService()


@router.post("/")
def create_user(
    user: UserCreate, user_service: UserService = Depends(get_user_service)
):
    return user_service.create_user(user)
