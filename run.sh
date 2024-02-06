#!/bin/sh

echo "creating virtual environment..."
python3 -m venv flaskenv

echo "printing command to activate the environment..."
echo ". flaskenv/bin/activate"

echo "install dependencies using the command below..."
echo "pip3 install -r requirements.txt"