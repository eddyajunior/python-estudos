from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_user_service
# from app.models import user
from app.models.user import UserCreate
# from app.services import user_service
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

@router.get("/{user_id}")
def get_user_by_id(
    user_id: int, 
    user_service: UserService = Depends(get_user_service)
):

    user = user_service.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.delete("/{user_id}")
def delete_user(
    user_id: int, 
    user_service: UserService = Depends(get_user_service)
):
    deleted = user_service.delete_user(user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": "User deleted successfully"}