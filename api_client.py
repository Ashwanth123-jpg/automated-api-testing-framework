
import time
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user(user_id=1):
    start_time = time.perf_counter()
    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        timeout=10
    )
    elapsed_ms = (time.perf_counter() - start_time) * 1000
    return response, round(elapsed_ms, 2)


def get_posts():
    start_time = time.perf_counter()
    response = requests.get(
        f"{BASE_URL}/posts",
        timeout=10
    )
    elapsed_ms = (time.perf_counter() - start_time) * 1000
    return response, round(elapsed_ms, 2)
