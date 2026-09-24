import requests
import time


def check_api(url):
    try:
        start_time = time.perf_counter()

        response = requests.get(url, timeout=10)

        end_time = time.perf_counter()

        response_time = round((end_time - start_time) * 1000, 2)

        return {
            "url": url,
            "status_code": response.status_code,
            "response_time": response_time,
            "status": "UP" if response.ok else "DOWN"
        }

    except requests.exceptions.RequestException as error:
        return {
            "url": url,
            "status_code": 0,
            "response_time": 0,
            "status": "DOWN",
            "error": str(error)
        }