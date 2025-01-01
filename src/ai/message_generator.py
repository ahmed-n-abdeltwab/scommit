"""AI-powered commit message generation module."""
from transformers import pipeline

class CommitMessageGenerator:
    def __init__(self):
        self.model = pipeline("text-generation", model="gpt2", device=-1)
    
    def generate(self, diff_text, max_length=50):
        """Generate a commit message from the diff text using GPT-2."""
        try:
            output = self.model(
                diff_text,
                max_new_tokens=max_length,
                num_return_sequences=1,
                do_sample=True,
                truncation=True,
            )
            
            message = output[0]['generated_text'].strip()
            return message if message else "Update code"
            
        except Exception as e:
            print("Error generating commit message:", e)
            return "Update code"
