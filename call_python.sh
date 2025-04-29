#!/bin/bash
#python git_commit_push.py -m "commit from shell script"
#python add_comment_and_commit.py helloworld.py -c "Added logging for debug" -m "Add comment for logging" -b main

RELATIVE_PATH="/mnt/imported/code/ticket-78656"
python $RELATIVE_PATH/add_comment_and_commit.py $RELATIVE_PATH/helloworld.py -c "Added logging for debug" -m "Add comment for logging" -b main

