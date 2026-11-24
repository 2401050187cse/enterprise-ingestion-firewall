
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import respond

app = FastAPI(
    title="Enterprise Ingestion Firewall",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(
    respond.router,
    prefix="/api"
)


@app.get("/")
async def root():
    return {
        "message": "Enterprise Ingestion Firewall API is running"
    }
