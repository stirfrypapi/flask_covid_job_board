#!/bin/bash
# job_boardrun
#
# Runs the flask server
set -Eeuo pipefail

# Test database
echo "+ test -e var/job_board.sqlite3"

#Call job_boarddb create if not database file exists
if  [ ! -e var/job_board.sqlite3 ]; then
    ./bin/job_board_db create
fi

#Set FLASK_DEBUG, FLASK_APP and INSTA485_SETTINGS environment variables
echo "+ export FLASK_DEBUG=True"
export FLASK_DEBUG=True
echo "+ FLASK_DEBUG=True"
FLASK_DEBUG=True
echo "+ export FLASK_APP=job_board"
export FLASK_APP=job_board
echo "+ FLASK_APP=job_board"
FLASK_APP=job_board
echo "+ export JOB_BOARD_SETTINGS=config.py"
export INSTA485_SETTINGS=config.py
echo "+ JOB_BOARD=config.py"
JOB_BOARD_SETTINGS=config.py

#Run the development server on port 8000
flask run --host 0.0.0.0 --port 8000