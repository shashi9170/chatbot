from typing import Any, Dict
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    thread_id: str
    usage: Dict[str, Any]