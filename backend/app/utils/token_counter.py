import tiktoken

def estimate_tokens(text: str) -> int:
    """Estimate token count using tiktoken (cl100k_base encoding)."""
    try:
        encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))
    except Exception:
        return len(text.split()) * 2
