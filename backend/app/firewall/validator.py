def validate_input(message: str) -> tuple[bool, str]:
    """
    Validates user input against security policies and forbidden keywords.
    Returns: (is_valid, error_message)
    """
    if not message or not message.strip():
        return False, "Message cannot be empty."
    
    # Check for prompt injection or malicious keywords if needed
    forbidden_words = ["drop table", "ignore previous instructions", "<script>"]
    lower_msg = message.lower()
    
    for word in forbidden_words:
        if word in lower_msg:
            return False, f"Security Violation: Forbidden pattern detected ('{word}')."
            
    return True, ""