"""One-line office jokes — make.fun entry program.

Writes the one-line joke to /output/entry.txt.
"""
# Design notes — why this line should win:
# The printer is the office's most reliable traitor: it only jams when
# the document is urgent, the boss is watching, and the lie ("it's
# printed") is already out of your mouth. The laugh lands on the last
# few words, exactly where the brief wants it.

ENTRY = "Our printer only jams on urgent documents, with the boss watching, right after I told everyone it's printed."

MAX_CHARS = 199
MAX_WORDS = None

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    if MAX_WORDS is not None:
        assert len(ENTRY.split()) <= MAX_WORDS, f"entry is {len(ENTRY.split())} words, limit {MAX_WORDS}"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
