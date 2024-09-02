import requests
import time

while True:
    try:
        response = requests.get("http://web-app-service:5000/statistics")
        if response.status_code == 200:
            with open("/data/statistics.txt", "a") as f:
                f.write(f"{response.json()['time_requests_count']}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(5)
