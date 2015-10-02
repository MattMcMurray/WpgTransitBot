#!/bin/bash

sudo bash << \EOF
echo "Installing python pip"
apt-get -y install python-pip

echo "Installing virtualenv"
pip install virtualenv

echo "Creating virtualenv"
virtualenv ../venv
source ../venv/bin/activate

echo "Installing dependencies"
pip install -U -r requirements.txt

echo "All done! You can now run the startbot.sh script"

EOF
