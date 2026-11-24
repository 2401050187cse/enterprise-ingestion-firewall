from pydantic import BaseModel
from typing import Optional

class ChatPayload(BaseModel):
    message: str
    summary: Optional[str] = "General Query"
    priority: Optional[str] = "Medium"
    session_id: str