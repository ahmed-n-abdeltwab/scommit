"""Tests for text cleaning utilities."""
import pytest
from src.ai.text_cleaner import clean_diff_text, clean_generated_message

def test_clean_diff_text_with_whitespace():
    """Test cleaning diff text with extra whitespace."""
    input_text = "  \n  Some diff text  \n  "
    assert clean_diff_text(input_text) == "Some diff text"

def test_clean_diff_text_empty():
    """Test cleaning empty diff text."""
    assert clean_diff_text("") == ""
    assert clean_diff_text(None) == ""

def test_clean_generated_message_normal():
    """Test cleaning a normal generated message."""
    message = "  Fix bug in login system  "
    assert clean_generated_message(message) == "Fix bug in login system"

def test_clean_generated_message_empty():
    """Test cleaning empty generated message."""
    assert clean_generated_message("") == "Update code"
    assert clean_generated_message("   ") == "Update code"

def test_clean_generated_message_custom_fallback():
    """Test cleaning with custom fallback message."""
    fallback = "Custom fallback"
    assert clean_generated_message("", fallback) == fallback
