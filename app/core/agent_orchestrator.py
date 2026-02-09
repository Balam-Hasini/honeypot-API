def run_agent(message, history):
    turns = len(history)

    if turns <= 1:
        return "Why will my account be blocked?"

    if "upi" in message.lower():
        return "I use PhonePe. Is that fine?"

    if turns <= 4:
        return "Can you explain once? I’m confused."

    if turns <= 7:
        return "I’m outside right now. Will it take long?"

    return "Okay, what details do you need exactly?"
   
