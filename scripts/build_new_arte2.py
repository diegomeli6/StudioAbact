import fitz, json, os, re

# Check for emojis
EMOJI_PATTERN = re.compile(
    "[\U00010000-\U0010ffff\uD800-\uDBFF\uDC00-\uDFFF\u2600-\u26FF\u2700-\u27BF]",
    flags=re.UNICODE
)

def assert_no_emojis(text, label=""):
    match = EMOJI_PATTERN.search(text)
    if match:
        raise ValueError(f"EMOJI FOUND in {label}: {match.group(0)} at pos {match.start()}")

print("Emoji checker ready")
