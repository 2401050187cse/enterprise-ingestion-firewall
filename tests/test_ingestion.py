import os
from dotenv import load5_dotenv

load_dotenv()

print("=== Task 1 Ingestion & Firewall Test ===")
print("GROQ_API_KEY loaded:", "Yes" if os.getenv("GROQ_API_KEY") else "No")
print("GROQ_MODEL:", os.getenv("GROQ_MODEL", "Not found"))
print("[SUCCESS] Test ingestion script executed successfully!")