#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Install dependencies (only if needed)
pip install --upgrade pip
pip install -r requirements.txt

# Run the main app
python main.py


