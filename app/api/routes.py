from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# -----------------------------
# MODELS
# -----------------------------

class Message(BaseModel):
    sender: str
    text: str

class HoneypotRequest(BaseModel):
    sessionId: str
    message: Message

class HoneypotResponse(BaseModel):
    status: str
    reply: str


# -----------------------------
# SIMPLE TEST ROUTE
# -----------------------------

@router.get("/test")
def test_api():
    return {"message": "FastAPI route is working successfully"}


# -----------------------------
# HONEYPOT API (MAIN)
# -----------------------------

API_KEY = "secret123"   # change if needed

@router.post("/honeypot/message", response_model=HoneypotResponse)
def honeypot_message(
    data: HoneypotRequest,
    x_api_key: Optional[str] = Header(None)
):
    # API key validation
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    scam_text = data.message.text.lower()

    # simple honeypot logic
    if "bank" in scam_text or "account" in scam_text:
        reply = "Why will my account be blocked?"
    elif "otp" in scam_text:
        reply = "I did not receive any OTP, can you resend?"
    else:
        reply = "Can you explain more details?"

    return {
        "status": "success",
        "reply": reply
    }
