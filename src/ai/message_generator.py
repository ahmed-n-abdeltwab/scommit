"""AI-powered commit message generation module."""
from transformers import pipeline
from .text_cleaner import clean_diff_text, clean_generated_message
from .model_config import ModelConfig

class CommitMessageGenerator:
    def __init__(self, config: ModelConfig = None):
        self.config = config or ModelConfig()
        self.model = pipeline(
            "text-generation",
            model=self.config.model_name,
            device=self.config.device
        )
    
    def generate(self, diff_text: str, max_length: int = 50) -> str:
        """Generate a commit message from the diff text."""
        try:
            cleaned_diff = clean_diff_text(diff_text)
            
            output = self.model(
                cleaned_diff,
                max_new_tokens=max_length,
                num_return_sequences=self.config.num_sequences,
                do_sample=self.config.do_sample,
                truncation=self.config.truncation
            )
            
            return clean_generated_message(output[0]['generated_text'])
            
        except Exception as e:
            print("Error generating commit message:", e)
            return "Update code"
