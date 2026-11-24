from typing import List, Dict

session_db: Dict[str, List[Dict[str, str]]] = {}

def get_history(session_id: str) -> List[Dict[str, str]]:
    if session_id not in session_db:
        session_db[session_id] = []
    return session_db[session_id]

def add_message(session_id: str, role: str, content: str):
    if session_id not in session_db:
        session_db[session_id] = []
    session_db[session_id].append({"role": role, "content": content})

def clear_session(session_id: str):
    if session_id in session_db:
        session_db[session_id] = []