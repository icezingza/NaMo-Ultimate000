import time
import requests
import json

def benchmark():
    url_interact = "http://localhost:8000/namo/interact"
    url_analyze = "http://localhost:8000/namo/analyze-emotion?text=I%20am%20happy"
    payload = {
        "user_id": "user123",
        "message": "I am happy"
    }
    headers = {"Content-Type": "application/json"}

    # Warmup
    for _ in range(5):
        requests.post(url_interact, json=payload, headers=headers)
        requests.post(url_analyze)

    n = 20

    start_time = time.time()
    for _ in range(n):
        requests.post(url_analyze)
    end_time = time.time()
    avg_analyze = (end_time - start_time) / n
    print(f"Average time for analyze-emotion: {avg_analyze:.4f}s")

    start_time = time.time()
    for _ in range(n):
        requests.post(url_interact, json=payload, headers=headers)
    end_time = time.time()
    avg_interact = (end_time - start_time) / n
    print(f"Average time for namo-interact: {avg_interact:.4f}s")

if __name__ == "__main__":
    benchmark()
