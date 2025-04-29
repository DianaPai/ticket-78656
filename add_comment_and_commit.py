import subprocess
import argparse
import sys
import os

def run_command(command, capture_output=False):
    result = subprocess.run(command, shell=True, capture_output=capture_output, text=True)
    if result.returncode != 0:
        sys.exit(f"Error running command: {command}\n{result.stderr}")
    return result.stdout.strip() if capture_output else None

def append_comment_to_file(file_path, comment):
    if not os.path.isfile(file_path):
        sys.exit(f"File not found: {file_path}")
    with open(file_path, "a") as f:
        f.write(f"\n# {comment}\n")
    print(f"✅ Comment added to {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Add a comment to a file and push to Git repo.")
    parser.add_argument("file", help="Path to the file to update")
    parser.add_argument("-c", "--comment", required=True, help="Comment to add to the file")
    parser.add_argument("-m", "--message", required=True, help="Git commit message")
    parser.add_argument("-b", "--branch", help="Branch to push to (default: current branch)")
    args = parser.parse_args()

    append_comment_to_file(args.file, args.comment)

    run_command(f"git add {args.file}")
    run_command(f'git commit -m "{args.message}"')

    branch = args.branch or run_command("git rev-parse --abbrev-ref HEAD", capture_output=True)
    run_command(f"git push origin {branch}")

    print("✅ Changes committed and pushed.")

if __name__ == "__main__":
    main()

