#!/bin/bash

# Check if a filename is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <filename> \"<commit message>\""
  exit 1
fi

# Add the file to the staging area
git add "$1"

# Check if a commit message is provided
if [ -z "$2" ]; then
  echo "No commit message provided. Committing with default message."
  git commit -m "Add $1"
else
  # Commit the changes with the provided message
  git commit -m "$2"
fi

echo "File '$1' added and committed successfully."
