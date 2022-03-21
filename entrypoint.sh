#!/bin/bash

PROJECT_NAME="Docker Conda base image"

# Sets script to fail if any command fails.
set -e

print_usage() {
echo "
$PROJECT_NAME

Usage:	$0 COMMAND

Options:
  help		        Print this help
  <command>		Run command
"
}

case "$1" in
    help)
        print_usage
        ;;
    run)
      	shift 1 ; echo
        exec "$@"
        ;;
    *)
	echo
        exec "$@"
esac
