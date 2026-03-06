from fastapi import APIRouter
from src.api.chat_routes import router as chat_router
from src.api.user_routes import router as user_router

api_router = APIRouter()

@api_router.get('/')
def default_route():
    return "hiiii"

api_router.include_router(chat_router, prefix="/chat", tags=["Chat"])
api_router.include_router(user_router, prefix="/users", tags=["Users"])