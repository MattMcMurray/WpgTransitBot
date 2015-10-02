#!/bin/bash

# This script assumes you're using a virtualenv in the directory above named 'venv'
source ../venv/bin/activate

python src/auth.py
nohup python src/bot.py &