from fastapi import APIRouter

from app.models.user import UserCreate
from app.services.user_service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["users"])

user_service = UserService()


@router.post("/")
def create_user(user: UserCreate):
    return user_service.create_user(user)
