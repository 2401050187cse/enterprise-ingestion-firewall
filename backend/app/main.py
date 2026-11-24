import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import respond

app = FastAPI(
    title="Enterprise Ingestion Firewall",
    version="1.0.0"
)

# Allowed frontend URLs
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000"
]

# Production frontend URL
frontend_url = os.getenv("FRONTEND_URL")

if frontend_url:
    origins.append(frontend_url.rstrip("/"))

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
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


@app.get("/health")
async def health():
    return {"status": "healthy"}