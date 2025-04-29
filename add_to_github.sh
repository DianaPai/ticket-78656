#!/bin/bash

# Check if a file name is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <file_name> [commit_message]"
  exit 1
fi

file_name="$1"
commit_message="${2:-Add $file_name}"

# Check if the file exists
if [ ! -f "$file_name" ]; then
  echo "Error: File '$file_name' not found."
  exit 1
fi

# Add the file to the staging area
git add "$file_name"

# Commit the changes
git commit -m "$commit_message"

# Push the changes to the remote repository
git push origin main
