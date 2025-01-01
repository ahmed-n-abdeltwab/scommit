"""AI-powered commit message generation module."""
from transformers import pipeline

class CommitMessageGenerator:
    def __init__(self):
        self.model = pipeline("text-generation", model="gpt2", device=-1)
    
    def generate(self, diff_text, max_length=50):
        """Generate a commit message from the diff text using GPT-2."""
        try:
            # Clean and prepare the input text
            cleaned_diff = diff_text.strip()
            
            output = self.model(
                cleaned_diff,
                max_new_tokens=max_length,
                num_return_sequences=1,
                do_sample=True,
                truncation=True
            )
            
            # Clean up the generated message
            message = output[0]['generated_text'].strip()
            # Ensure we have a valid message
            return message if message else "Update code"
            
        except Exception as e:
            print("Error generating commit message:", e)
            return "Update code"
