#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a filename as an argument."
    exit 1
fi

python -u "$1" < /dev/tty