def classify_slide(content):
    keywords = {
        "cover": ["title", "introduction"],
        "result": ["result", "accuracy"],
        "flow": ["process", "workflow"]
    }
    for k,v in keywords.items():
        if any(word in content.lower() for word in v):
            return k
    return "general"
