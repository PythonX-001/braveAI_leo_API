from typing import Optional
from dataclasses import dataclass

@dataclass
class LeoCompleteResponse:
    completion: str
    stop_reason: Optional[str]
    truncated: bool
    stop: Optional[str]
    model: str
    log_id: str
    exception: Optional[str]