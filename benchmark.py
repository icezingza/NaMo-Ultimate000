import requests
import time
import json

def benchmark():
    url = "http://localhost:8000/namo/interact"
    payload = {
        "user_id": "user123",
        "message": "ผมรู้สึกเหงาและเศร้ามากในวันนี้"
    }
    headers = {"Content-Type": "application/json"}

    # Warm up
    print("Warming up...")
    for _ in range(2):
        try:
            requests.post(url, json=payload, headers=headers, timeout=60)
        except:
            pass

    print("Benchmarking...")
    latencies = []
    for i in range(10):
        start = time.time()
        response = requests.post(url, json=payload, headers=headers)
        end = time.time()
        latencies.append((end - start) * 1000)
        print(f"Request {i+1}: {latencies[-1]:.2f}ms")

    avg_latency = sum(latencies) / len(latencies)
    print(f"\nAverage Latency: {avg_latency:.2f}ms")

if __name__ == "__main__":
    benchmark()
