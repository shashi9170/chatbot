from fastapi import APIRouter, Depends

from src.schemas.chat_schema import ChatRequest, ChatResponse
from src.services.chat_service import ChatService
from src.dependencies.memory_dep import get_memory_context

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest, memory=Depends(get_memory_context)):
    
    service = ChatService(memory)
    response = service.chat(request.message, request.thread_id)

    return {"response": response}