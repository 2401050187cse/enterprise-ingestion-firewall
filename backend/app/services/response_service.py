
from app.services.memory_service import get_history, add_message
from app.services.llm_service import generate_llm_response


def generate_ai_response(
    message: str,
    summary: str,
    priority: str,
    session_id: str
) -> str:

    # Get previous conversation history
    history = get_history(session_id)

    # Create dynamic system prompt
    system_prompt = f"""
    You are an Enterprise Support AI Assistant.

    User Context:
    Summary: {summary}
    Priority: {priority}

    Instructions:
    1. Understand the user's question.
    2. Provide accurate and helpful answers.
    3. Use simple English.
    4. Format responses using Markdown.
    5. Consider previous conversation history.
    """

    # Prepare messages for Groq
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # Add previous conversation
    messages.extend(history)

    # Add current user message
    messages.append({
        "role": "user",
        "content": message
    })

    # Generate AI response
    bot_reply = generate_llm_response(messages)

    # Save conversation history
    add_message(session_id, "user", message)
    add_message(session_id, "assistant", bot_reply)

    return bot_reply
