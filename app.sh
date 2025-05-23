#!/usr/bin/env bash

# app.sh from the main branch
# This is a bash script for Domino's App publishing feature
#   learn more at http://support.dominodatalab.com/hc/en-us/articles/209150326
 
## Python/Flask example
#export LC_ALL=C.UTF-8
#export LANG=C.UTF-8
#export FLASK_APP=app-flask.py
#export FLASK_DEBUG=1
#python -m flask run --host=0.0.0.0 --port=8888
 
## Dash example
#python app-dash.py
#python app.py
 
## R/Shiny example
R -e 'shiny::runApp("./", port=8888, host="0.0.0.0")'
##