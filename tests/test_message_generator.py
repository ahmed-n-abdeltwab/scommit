"""Tests for commit message generation."""
import pytest
from unittest.mock import Mock, patch
from src.ai.message_generator import CommitMessageGenerator
from src.ai.model_config import ModelConfig

@pytest.fixture
def mock_pipeline():
    """Create a mock pipeline for testing."""
    with patch('src.ai.message_generator.pipeline') as mock:
        yield mock

def test_message_generator_initialization(mock_pipeline):
    """Test CommitMessageGenerator initialization."""
    config = ModelConfig(model_name="test-model")
    generator = CommitMessageGenerator(config)
    
    mock_pipeline.assert_called_once_with(
        "text-generation",
        model="test-model",
        device=-1
    )

def test_generate_successful_message(mock_pipeline):
    """Test successful message generation."""
    # Setup mock pipeline
    mock_model = Mock()
    mock_model.return_value = [{'generated_text': " Generated commit message "}]
    mock_pipeline.return_value = mock_model
    
    # Create generator and generate message
    generator = CommitMessageGenerator()
    message = generator.generate("test diff", max_length=50)
    
    assert message == "Generated commit message"
    mock_model.assert_called_once_with(
        "test diff",
        max_new_tokens=50,
        num_return_sequences=1,
        do_sample=True,
        truncation=True
    )

def test_generate_handles_exception(mock_pipeline):
    """Test error handling during message generation."""
    # Setup mock pipeline to raise an exception
    mock_model = Mock(side_effect=Exception("Test error"))
    mock_pipeline.return_value = mock_model
    
    # Create generator and generate message
    generator = CommitMessageGenerator()
    message = generator.generate("test diff")
    
    assert message == "Update code"
