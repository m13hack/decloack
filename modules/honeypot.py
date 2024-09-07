import requests

def setup_honeypot():
    print("\033[92mSetting up Honeypot...\033[0m")
    try:
        honeypot_url = input("\033[93mEnter honeypot URL:\033[0m ")
        response = requests.get(honeypot_url)
        
        if response.status_code == 200:
            print(f"\033[92mHoneypot is successfully set up and monitoring at:\033[0m {honeypot_url}")
        else:
            raise RuntimeError("\033[91mFailed to reach the honeypot URL.\033[0m")
    
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"\033[91mFailed to set up honeypot: {e}\033[0m")
    except Exception as e:
        raise RuntimeError(f"\033[91mError occurred during honeypot setup: {e}\033[0m")
