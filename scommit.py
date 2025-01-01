import subprocess
import os
from transformers import pipeline

def get_git_diff(project_path):
    try:
        # Change to the target project's directory
        os.chdir(project_path)
        diff = subprocess.check_output(["git", "diff", "--staged"], stderr=subprocess.STDOUT)
        return diff.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print("Error getting git diff:", e.output.decode("utf-8"))
        return ""
    except FileNotFoundError:
        print("Invalid project path or git is not initialized.")
        return ""

def generate_commit_message(diff_text, max_length=50):
    try:
        summarizer = pipeline("text-generation", model="gpt2", device=-1)  # Use CPU
        output = summarizer(
            diff_text,
            max_length=max_length,  # Use user-provided max_length
            num_return_sequences=1,
            do_sample=True
        )
        return output[0]['generated_text']
    except Exception as e:
        print("Error generating commit message:", e)
        return ""

def commit_changes(commit_message):
    try:
        result = subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True, text=True)
        print("Changes committed successfully.")
        print("Commit Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error committing changes:", e)
        print("Commit Error Output:", e.stderr)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate a commit message from staged git changes.")
    parser.add_argument("project_path", type=str, help="Path to the target project directory.")
    parser.add_argument("--max_length", type=int, default=50, help="Maximum length for the generated commit message.")
    args = parser.parse_args()

    # Step 1: Get the git diff
    diff_text = get_git_diff(args.project_path)

    if not diff_text:
        print("No changes staged for commit or invalid project path.")
    else:
        # Step 2: Generate a commit message
        commit_message = generate_commit_message(diff_text, max_length=args.max_length)

        # Step 3: Commit the changes with the generated message
        commit_changes(commit_message)

