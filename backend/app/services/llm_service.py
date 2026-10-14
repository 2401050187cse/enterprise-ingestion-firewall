import instructor
from groq import Groq
from backend.app.config import settings
from backend.app.schemas.ingestion import IngestionResult, TokenMetadata
from backend.app.utils.token_counter import estimate_tokens

def analyze_message(message: str) -> IngestionResult:
    client = instructor.from_groq(Groq(api_key=settings.GROQ_API_KEY))

    prompt = f"""
    Analyze the following customer support message and classify it according to the schema.
    Message: "{message}"
    """

    result: IngestionResult = client.chat.completions.create(
        model=settings.GROQ_MODEL,
        response_model=IngestionResult,
        messages=[
            {"role": "system", "content": "You are an enterprise support request classifier and ingestion firewall."},
            {"role": "user", "content": prompt}
        ],
        max_retries=2
    )

    input_tokens = estimate_tokens(message)
    result.token_metadata = TokenMetadata(
        estimated_input_tokens=input_tokens,
        note="Estimated locally; may differ from provider token counts."
    )

    return result
