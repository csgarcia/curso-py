from pathlib import Path

file = Path("files/test-file.txt")

text = file.read_text("utf-8").split("\n")
text.insert(0, "New line at the top")
file.write_text("\n".join(text), "utf-8")
