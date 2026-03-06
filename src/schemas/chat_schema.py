from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    thread_id: str

class ChatResponse(BaseModel):
    response: str

# from typing import List, TypedDict
# from langchain_core.messages import BaseMessage

# class ChatState(TypedDict):
#     messages: List[BaseMessage]