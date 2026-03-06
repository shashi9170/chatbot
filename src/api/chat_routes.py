import uuid
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from src.schemas.chat_schema import ChatRequest, ChatResponse
from src.services.chat_service import ChatService
from src.dependencies.memory_dep import get_memory_context

router = APIRouter()

# Starts a new chat session by generating a thread_id and processing the user message
@router.post("", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest, memory=Depends(get_memory_context)):
    thread_id = str(uuid.uuid4())
    service = ChatService(memory)
    response = service.chat(request.message, thread_id)

    return {"response": response, "thread_id": thread_id}


# Continues an existing chat session by processing the message with thread memory
@router.post("/{thread_id}", response_model=ChatResponse)
def chat_existing(thread_id: str, request: ChatRequest, memory=Depends(get_memory_context)):

    service = ChatService(memory)

    response = service.chat(request.message, thread_id)

    return {
         **response,
        "thread_id": thread_id
    }
    
    
# Starts a new chat session and streams the AI response
@router.post("/stream")
def stream_new_chat(request: ChatRequest, memory=Depends(get_memory_context)):

    thread_id = str(uuid.uuid4())
    service = ChatService(memory)
    generator = service.stream_chat(request.message, thread_id)

    return StreamingResponse(generator, media_type="text/event-stream")


# Continues an existing chat session and streams the AI response
@router.post("/{thread_id}/stream")
def stream_existing_chat(thread_id: str, request: ChatRequest, memory=Depends(get_memory_context)):

    service = ChatService(memory)
    generator = service.stream_chat(request.message, thread_id)

    return StreamingResponse(generator, media_type="text/event-stream")