SCAM_KEYWORDS = [
    "account blocked", "urgent", "verify",
    "upi", "otp", "kyc", "bank", "suspend", "share"
]

def detect_scam(text: str):
    score = 0
    text = text.lower()

    for word in SCAM_KEYWORDS:
        if word in text:
            score += 1

    return {
        "is_scam": score >= 1,   # 👈 KEY CHANGE
        "confidence": min(score * 30, 100)
    }
