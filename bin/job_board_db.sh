#!/bin/bash
# job_boarddb

# Stop on errors
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail

# Sanity check command line options
usage() {
  echo "Usage: $0 (create|destroy|reset|dump)"
}

if [ $# -ne 1 ]; then
  usage
  exit 1
fi

# Parse argument.  $1 is the first argument
case $1 in
  "create")
    if [ ! -e var/job_board.sqlite3 ]; then
      echo "+ mkdir -p var/uploads"
      mkdir -p var/uploads
      echo "+ sqlite3 var/job_board.sqlite3 < sql/schema.sql"
      sqlite3 var/job_board.sqlite3 < sql/schema.sql
      echo "+ sqlite3 var/job_board.sqlite3 < sql/data.sql"
      sqlite3 var/job_board.sqlite3 < sql/data.sql
    else
      echo "Error: database already exists"
      exit 1
    fi
    ;;

  "destroy")
    echo "+ rm -rf var/job_board.sqlite3"
    rm -rf var/job_board.sqlite3
    ;;

  "reset")
    echo "+ rm -rf var/job_board.sqlite3"
    rm -rf var/job_board.sqlite3
    echo "+ sqlite3 var/job_board.sqlite3 < sql/schema.sql"
    sqlite3 var/job_board.sqlite3 < sql/schema.sql
    echo "+ sqlite3 var/job_board.sqlite3 < sql/data.sql"
    sqlite3 var/job_board.sqlite3 < sql/data.sql
    ;;

  "dump")
    sqlite3 -batch -line var/job_board.sqlite3 'SELECT * FROM accounts'
    sqlite3 -batch -line var/job_board.sqlite3 'SELECT * FROM applicants'
    sqlite3 -batch -line var/job_board.sqlite3 'SELECT * FROM applications'
    sqlite3 -batch -line var/job_board.sqlite3 'SELECT * FROM employers'
    sqlite3 -batch -line var/job_board.sqlite3 'SELECT * FROM openings'
    ;;
  *)
    exit 1
    ;;
esac