from pydantic import BaseModel, Field
from typing import Literal, Optional

class IngestionRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Customer support message to classify")

class TokenMetadata(BaseModel):
    estimated_input_tokens: int = Field(..., description="Estimated number of input tokens")
    note: str = Field(..., description="Disclaimer note about token estimation")

class IngestionResult(BaseModel):
    intent: Literal["greeting", "order_tracking", "payment_issue", "current_time", "general_question", "unknown"] = Field(
        ..., description="Classified intent of the message"
    )
    risk_profile: Literal["low", "medium", "high"] = Field(..., description="Assessed risk profile")
    priority: Literal["low", "medium", "high"] = Field(..., description="Urgency/priority level")
    requires_action: bool = Field(..., description="Whether human or system action is required")
    summary: str = Field(..., description="Concise summary of the customer message")
    token_metadata: Optional[TokenMetadata] = Field(default=None, description="Token usage estimation metadata")
