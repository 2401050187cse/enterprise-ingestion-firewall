from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.app.schemas.ingestion import IngestionRequest, IngestionResult
from backend.app.services.llm_service import analyze_message

app = FastAPI(
    title="Enterprise Structured Ingestion Firewall",
    description="Classifies customer support messages and validates output using Pydantic and Instructor.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "running", "service": "Enterprise Structured Ingestion Firewall"}

@app.post("/api/analyze", response_model=IngestionResult)
def analyze_endpoint(payload: IngestionRequest):
    try:
        result = analyze_message(payload.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
