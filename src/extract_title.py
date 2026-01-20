def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip()
    raise Exception("Could not find title in markdown")
