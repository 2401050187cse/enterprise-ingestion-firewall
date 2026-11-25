from typing import List, Dict
from app.services.database_service import supabase


def get_history(session_id: str) -> List[Dict[str, str]]:
    result = (
        supabase.table("chat_history")
        .select("role, content")
        .eq("session_id", session_id)
        .order("id")
        .execute()
    )

    return result.data or []


def add_message(session_id: str, role: str, content: str):
    supabase.table("chat_history").insert({
        "session_id": session_id,
        "role": role,
        "content": content
    }).execute()


def clear_session(session_id: str):
    supabase.table("chat_history").delete().eq(
        "session_id", session_id
    ).execute()
