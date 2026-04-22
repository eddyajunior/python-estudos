from fastapi import APIRouter, Depends

from app.api.dependencies import get_user_service
from app.models.user import UserCreate
from app.services.user_service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["users"])


@router.post("/")
def create_user(
    user: UserCreate, user_service: UserService = Depends(get_user_service)
):
    return user_service.create_user(user)


@router.get("/")
def list_users(user_service: UserService = Depends(get_user_service)):
    return user_service.list_users()
