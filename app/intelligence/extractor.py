import re

intel_db = {}

def extract_intelligence(session_id, text):
    if session_id not in intel_db:
        intel_db[session_id] = {
            "upiIds": [],
            "phoneNumbers": [],
            "links": [],
            "keywords": []
        }

    intel_db[session_id]["upiIds"] += re.findall(r'\b[\w.-]+@upi\b', text)
    intel_db[session_id]["phoneNumbers"] += re.findall(r'\+91\d{10}', text)
    intel_db[session_id]["links"] += re.findall(r'https?://\S+', text)

    for k in ["urgent", "verify", "blocked"]:
        if k in text.lower():
            intel_db[session_id]["keywords"].append(k)
