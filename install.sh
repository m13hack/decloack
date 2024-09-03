#!/bin/bash

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies (if you have a requirements.txt, uncomment the next line)
# pip install -r requirements.txt

echo "Dependencies are installed and virtual environment is set up."

# If you need additional system packages, you can add them here. For example:
# sudo apt-get update
# sudo apt-get install -y some-package

echo "Setup complete."
