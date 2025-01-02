"""Tests for model configuration."""
import pytest
from src.ai.model_config import ModelConfig

def test_default_config():
    """Test default model configuration."""
    config = ModelConfig()
    assert config.model_name == "gpt2"
    assert config.device == -1
    assert config.do_sample is True
    assert config.truncation is True
    assert config.num_sequences == 1

def test_custom_config():
    """Test custom model configuration."""
    config = ModelConfig(
        model_name="custom-model",
        device=0,
        do_sample=False,
        truncation=False,
        num_sequences=2
    )
    assert config.model_name == "custom-model"
    assert config.device == 0
    assert config.do_sample is False
    assert config.truncation is False
    assert config.num_sequences == 2
