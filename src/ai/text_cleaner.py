"""Text preprocessing utilities for commit messages."""

def clean_diff_text(diff_text: str) -> str:
    """Clean and prepare diff text for processing."""
    return diff_text.strip() if diff_text else ""

def clean_generated_message(message: str, fallback: str = "Update code") -> str:
    """Clean and validate the generated message."""
    cleaned = message.strip()
    return cleaned if cleaned else fallback
