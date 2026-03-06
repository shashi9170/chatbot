from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def user():
    return {"message": "User endpoint"}