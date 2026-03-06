from typing import Any, Dict
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str


class TokenUsage(BaseModel):
    input_tokens: int
    output_tokens: int
    total_tokens: int
    input_token_details: Dict[str, int] = {}
    output_token_details: Dict[str, int] = {}

class ChatResponse(BaseModel):
    response: str
    thread_id: str
    usage: TokenUsage