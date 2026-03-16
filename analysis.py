def extract_category(text):
    for line in text.split("\n"):
        if line.startswith("Category:"):
            return line.replace("Category:", "").strip()
    return "-"


def extract_priority(text):
    for line in text.split("\n"):
        if line.startswith("Priority:"):
            return line.replace("Priority:", "").strip()
    return "-"
