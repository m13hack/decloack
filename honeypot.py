import requests

def setup_honeypot():
    print("\033[92mSetting up Honeypot...\033[0m")
    try:
        honeypot_url = input("\033[93mEnter honeypot URL:\033[0m ")
        response = requests.get(honeypot_url)
        print(f"\033[92mMonitoring traffic at honeypot: {response.content}\033[0m")
    except Exception as e:
        raise RuntimeError(f"Failed to set up honeypot: {e}")
