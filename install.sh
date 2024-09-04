#!/bin/bash

# Exit script on error
set -e

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install dependencies from requirements.txt if it exists
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping dependency installation from requirements.txt."
fi

# Print message indicating that dependencies are installed and virtual environment is set up
echo "Dependencies are installed and virtual environment is set up."

# If additional system packages are needed, uncomment and modify the lines below
# Update package list and install additional system packages
# sudo apt-get update
# sudo apt-get install -y some-package

# If using a different package manager (like yum, dnf, or brew), adjust accordingly
# For example, on macOS with Homebrew:
# brew install some-package

# Print a message indicating that the setup is complete
echo "Setup complete."
