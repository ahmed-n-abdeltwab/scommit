"""Configuration for the AI model."""
from dataclasses import dataclass

@dataclass
class ModelConfig:
    model_name: str = "gpt2"
    device: int = -1  # -1 for CPU
    do_sample: bool = True
    truncation: bool = True
    num_sequences: int = 1
