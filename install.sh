#!/bin/bash

echo "-------------------------------------------------"
echo "     Installing Dependencies for TorDeAnonymizer"
echo "-------------------------------------------------"

# Ensure Python and pip are installed
if ! [ -x "$(command -v python3)" ]; then
    echo "Python3 is not installed. Installing it..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

if ! [ -x "$(command -v pip3)" ]; then
    echo "pip is not installed. Installing it..."
    sudo apt-get install -y python3-pip
fi

# Install Python dependencies
pip3 install -r requirements.txt

# Check if Tor is installed
if ! [ -x "$(command -v tor)" ]; then
    echo "Tor is not installed. Installing Tor..."
    sudo apt-get install -y tor
fi

echo "-------------------------------------------------"
echo "     Setup Complete! Run the tool using:"
echo "     python3 decloack.py"
echo "-------------------------------------------------"
