from pydantic import BaseModel
from typing import List

class OSRResponse(BaseModel):
    primaryOutcome: str
    performanceTargets: List[str]
    supportOutcomes: List[str]
    flowRates: List[str]
    milestones: List[str]
