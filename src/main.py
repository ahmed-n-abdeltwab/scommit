"""Main entry point for the smart commit message generator."""
from cli.argument_parser import create_parser
from git.git_operations import get_staged_diff, commit_changes
from ai.message_generator import CommitMessageGenerator

def main():
    # Parse command line arguments
    parser = create_parser()
    args = parser.parse_args()

    # Get staged changes
    diff_text = get_staged_diff(args.project_path)
    if not diff_text:
        print("No changes staged for commit or invalid project path.")
        return

    # Generate commit message
    generator = CommitMessageGenerator()
    commit_message = generator.generate(diff_text, max_length=args.max_length)

    # Commit changes
    commit_changes(commit_message)

if __name__ == "__main__":
    main()