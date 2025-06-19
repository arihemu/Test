
def is_palindrome(s: str) -> bool:
    """Return True if the given string is a palindrome, False otherwise."""
    normalized = ''.join(ch.lower() for ch in s if ch.isalnum())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    examples = [
        "racecar",
        "Hello",
        "A man, a plan, a canal, Panama",
    ]
    for text in examples:
        print(f"{text!r} -> {is_palindrome(text)}")
