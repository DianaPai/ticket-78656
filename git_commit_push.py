import subprocess
import argparse
import sys

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        sys.exit(f"Error running command: {command}")

def main():
    parser = argparse.ArgumentParser(description="Commit and push changes to a Git repository.")
    parser.add_argument("-m", "--message", required=True, help="Commit message")
    args = parser.parse_args()

    print("Adding changes...")
    run_command("git add .")

    print(f"Committing with message: {args.message}")
    run_command(f'git commit -m "{args.message}"')

    print("Pushing to remote repository...")
    run_command("git push")

    print("Done!")

if __name__ == "__main__":
    main()

# test commit
