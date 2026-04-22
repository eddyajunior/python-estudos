from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["hello"])


@router.get("/hello")
def hello():
    return {"message": "Olá, API!"}
