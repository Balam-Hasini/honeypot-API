sessions = {}

def store_message(session_id, sender, text):
    if session_id not in sessions:
        sessions[session_id] = []
    sessions[session_id].append({
        "sender": sender,
        "text": text
    })

def get_history(session_id):
    return sessions.get(session_id, [])
