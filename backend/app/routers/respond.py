from fastapi import APIRouter, HTTPException
from app.schemas.payload import ChatPayload
from app.firewall.validator import validate_input
from app.services.response_service import generate_ai_response
from app.services.memory_service import clear_session

router = APIRouter()

@router.post("/respond")
async def handle_chat(payload: ChatPayload):
    # Firewall input validation
    is_valid, err_msg = validate_input(payload.message)
    if not is_valid:
        raise HTTPException(status_code=400, detail=err_msg)

    reply = generate_ai_response(
        message=payload.message,
        summary=payload.summary,
        priority=payload.priority,
        session_id=payload.session_id
    )
    return {"status": "success", "response": reply, "session_id": payload.session_id}

@router.post("/clear")
async def handle_clear(payload: dict):
    session_id = payload.get("session_id")
    if session_id:
        clear_session(session_id)
    return {"status": "success", "message": f"Session {session_id} cleared"}