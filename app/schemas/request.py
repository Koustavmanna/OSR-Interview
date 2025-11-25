from pydantic import BaseModel, Field

class OSRRequest(BaseModel):
    description: str = Field(..., min_length=5)
