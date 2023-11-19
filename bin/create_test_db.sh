#!/bin/zsh

########################################
#   Creates and populates production DB
#       Parameter $1 - DB filename
#########################################

if [ -f "$1" ]; 
then
    rm "$1"
fi

app/python/tests/generate_fakes.py
