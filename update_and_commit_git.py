import subprocess

def update_and_commit_git(commit_message):
    try:
        # Pull changes from the remote repository
        subprocess.run(['git', 'pull'], check=True, capture_output=True)
        
        # Add all changes
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        
        # Commit changes
        subprocess.run(['git', 'commit', '-m', commit_message], check=True, capture_output=True)
        
        # Push changes to the remote repository
        subprocess.run(['git', 'push'], check=True, capture_output=True)
        
        print("Git repository updated and committed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during git operation: {e}")
        print(f"Stderr: {e.stderr.decode()}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    message = input("Enter commit message: ")
    update_and_commit_git(message)
