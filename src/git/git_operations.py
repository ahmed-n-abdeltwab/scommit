"""Git operations module for handling git-related functionality."""
import subprocess
import os

def get_staged_diff(project_path):
    """Get the staged changes in the git repository."""
    try:
        os.chdir(project_path)
        diff = subprocess.check_output(["git", "diff", "--staged"], stderr=subprocess.STDOUT)
        return diff.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print("Error getting git diff:", e.output.decode("utf-8"))
        return ""
    except FileNotFoundError:
        print("Invalid project path or git is not initialized.")
        return ""

def commit_changes(commit_message):
    """Commit staged changes with the provided message."""
    try:
        result = subprocess.run(
            ["git", "commit", "-m", commit_message], 
            check=True, 
            capture_output=True, 
            text=True
        )
        print("Changes committed successfully.")
        print("Commit Output:", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("Error committing changes:", e)
        print("Commit Error Output:", e.stderr)
        return False