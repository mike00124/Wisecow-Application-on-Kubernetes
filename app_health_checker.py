import requests
import time

# Configuration
URL = "http://yourapplicationurl.com"
CHECK_INTERVAL = 60  # seconds

def check_health():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print(f"{time.ctime()}: Application is UP")
        else:
            print(f"{time.ctime()}: Application is DOWN - Status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"{time.ctime()}: Application is DOWN - Unable to connect")

if __name__ == "__main__":
    while True:
        check_health()
        time.sleep(CHECK_INTERVAL)
