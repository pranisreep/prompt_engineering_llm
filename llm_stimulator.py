def call_claude(prompt):
    if "payment" in prompt.lower() or "charged" in prompt.lower() or "refund" in prompt.lower():
        if "Reasoning" in prompt:
            return "Reasoning: User reports being charged despite payment failure — clear billing issue.\nCategory: Billing\nPriority: High"
        return "Category: Billing\nPriority: High"

    elif "crash" in prompt.lower() or "error" in prompt.lower():
        if "Reasoning" in prompt:
            return "Reasoning: App crashing consistently is a software defect affecting core functionality.\nCategory: Bug\nPriority: High"
        return "Category: Bug\nPriority: High"

    elif "slow" in prompt.lower() or "seconds" in prompt.lower() or "load" in prompt.lower():
        if "Reasoning" in prompt:
            return "Reasoning: Sudden performance degradation suggests a backend issue.\nCategory: Performance\nPriority: Medium"
        return "Category: Performance\nPriority: Medium"

    elif "dark mode" in prompt.lower() or "add" in prompt.lower():
        if "Reasoning" in prompt:
            return "Reasoning: User is requesting a new UI feature — not a bug, low urgency.\nCategory: Feature Request\nPriority: Low"
        return "Category: Feature Request\nPriority: Low"

    elif "account" in prompt.lower() or "country" in prompt.lower():
        if "Reasoning" in prompt:
            return "Reasoning: Unauthorized account access is a potential security breach — critical urgency.\nCategory: Security\nPriority: Critical"
        return "Category: Security\nPriority: Critical"

    else:
        return "Category: General\nPriority: Low"
