"""
Add to orchestrator/api.py - Meta² Onboarding Endpoint
"""

from fastapi import APIRouter
from pydantic import BaseModel
from .onboard_feature import onboard_user

router = APIRouter()

class OnboardRequest(BaseModel):
    user_id: str
    include_history: bool = True

@router.post("/orchestrator/onboard")
async def onboard_endpoint(request: OnboardRequest):
    """
    Onboard new user by learning from their shell history
    
    Returns personalized agent configuration
    """
    result = onboard_user(request.user_id)
    
    return {
        "run_id": f"onboard-{request.user_id}",
        "reply": f"Onboarded user {request.user_id}",
        "bits": {"A": 1, "U": 0, "P": 1, "E": 0, "delta": 0, "I": 0, "R": 0, "T": 1, "M": 0},
        "status": "executed",
        "status_line": "user onboarded; agent configured",
        "onboarding_data": result
    }

# Usage examples:
"""
# Onboard a new user
curl -X POST http://127.0.0.1:8080/orchestrator/onboard \
  -H "X-API-Key: change-me" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "dev123"}'

# Response includes:
{
  "onboarding_data": {
    "profile": {
      "command_count": 2874,
      "patterns": {...},
      "preferences": {"preferred_editor": "vscode"},
      "tools": ["git", "curl", "python"]
    },
    "agent_config": {
      "suggested_tools": [...],
      "custom_prompts": [...],
      "workflow_templates": [...]
    }
  }
}
"""
