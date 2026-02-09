import requests

def send_final_result(payload):
    requests.post(
        "https://hackathon.guvi.in/api/updateHoneyPotFinalResult",
        json=payload,
        timeout=5
    )
