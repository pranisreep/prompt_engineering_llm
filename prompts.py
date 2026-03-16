from llm_simulator import call_claude

def zero_shot(ticket):
    prompt = f"""Classify this support ticket into one category:
Billing, Bug, Performance, Feature Request, Security, General.

Also give a priority: Critical, High, Medium, Low.

Format:
Category: <category>
Priority: <priority>

Ticket: {ticket}"""
    return call_claude(prompt)


def few_shot(ticket):
    prompt = f"""Classify this support ticket.

Examples:
Ticket: I was double-charged.
Category: Billing
Priority: High

Ticket: App crashes on login.
Category: Bug
Priority: High

Now classify this ticket:

Ticket: {ticket}"""
    return call_claude(prompt)


def chain_of_thought(ticket):
    prompt = f"""Think step by step.

Format:
Reasoning: <reason>
Category: <category>
Priority: <priority>

Ticket: {ticket}"""
    return call_claude(prompt)
