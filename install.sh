#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}-------------------------------------------------${NC}"
echo -e "${GREEN}     Installing Dependencies for TorDeAnonymizer ${NC}"
echo -e "${GREEN}-------------------------------------------------${NC}"

# Ensure Python and pip are installed
if ! [ -x "$(command -v python3)" ]; then
    echo -e "${YELLOW}Python3 is not installed. Installing it...${NC}"
    sudo apt-get update
    sudo apt-get install -y python3
fi

if ! [ -x "$(command -v pip3)" ]; then
    echo -e "${YELLOW}pip3 is not installed. Installing it...${NC}"
    sudo apt-get install -y python3-pip
fi

# Install Python dependencies
pip3 install -r requirements.txt

# Check if Tor is installed
if ! [ -x "$(command -v tor)" ]; then
    echo -e "${YELLOW}Tor is not installed. Installing Tor...${NC}"
    
    # Add Tor repository
    sudo add-apt-repository universe
    sudo apt update
    sudo apt install apt-transport-https
    sudo apt install -y dirmngr
    gpg --keyserver keys.openpgp.org --recv 04EE7237B7D453EC
    gpg --export 04EE7237B7D453EC | sudo apt-key add -
    echo "deb https://deb.torproject.org/torproject.org $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/tor.list
    sudo apt update
    sudo apt install tor -y
fi

# Install Wireshark (for pyshark)
if ! [ -x "$(command -v tshark)" ]; then
    echo -e "${YELLOW}tshark is not installed. Installing Wireshark...${NC}"
    sudo apt-get install -y tshark
    sudo usermod -aG wireshark $(whoami) # Allow non-root users to capture packets
fi

if [ $? -eq 0 ]; then
    echo -e "${GREEN}-------------------------------------------------${NC}"
    echo -e "${GREEN}     Setup Complete! Run the tool using:${NC}"
    echo -e "${GREEN}     python3 decloack.py${NC}"
    echo -e "${GREEN}-------------------------------------------------${NC}"
else
    echo -e "${RED}Error: Installation failed.${NC}"
fi
