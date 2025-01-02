"""Command line argument parsing module."""
import argparse

def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate a commit message from staged git changes."
    )
    parser.add_argument(
        "project_path",
        type=str,
        help="Path to the target project directory."
    )
    parser.add_argument(
        "--max_length",
        type=int,
        default=50,
        help="Maximum length for the generated commit message."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the generated message without committing changes."
    )
    return parser
