
import csv
import os
import time
import pytest

from api_client import get_user, get_posts

REPORT_DIR = "reports"
REPORT_FILE = os.path.join(REPORT_DIR, "api_test_report.csv")


def run_api_checks():
    results = []

    checks = [
        ("User status code", "Positive", lambda: check_user_status()),
        ("User JSON format", "Positive", lambda: check_user_json()),
        ("User required fields", "Validation", lambda: check_user_fields()),
        ("User address and company", "Validation", lambda: check_user_details()),
        ("Missing user returns 404", "Negative", lambda: check_missing_user()),
        ("Posts status code", "Positive", lambda: check_posts_status()),
        ("Posts response is a list", "Validation", lambda: check_posts_list()),
        ("Post required fields", "Validation", lambda: check_post_fields()),
        ("Post IDs are unique", "Validation", lambda: check_unique_post_ids()),
        ("Response time is measured", "Performance", lambda: check_response_time()),
    ]

    for name, category, check in checks:
        started = time.perf_counter()
        try:
            check()
            status = "PASS"
            details = ""
        except Exception as exc:
            status = "FAIL"
            details = str(exc)

        duration_ms = round((time.perf_counter() - started) * 1000, 2)
        results.append({
            "test_name": name,
            "category": category,
            "status": status,
            "duration_ms": duration_ms,
            "details": details,
        })

    os.makedirs(REPORT_DIR, exist_ok=True)

    with open(REPORT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "test_name",
                "category",
                "status",
                "duration_ms",
                "details",
            ],
        )
        writer.writeheader()
        writer.writerows(results)

    passed = sum(item["status"] == "PASS" for item in results)
    failed = sum(item["status"] == "FAIL" for item in results)

    print(f"\nReport saved to: {REPORT_FILE}")
    print(f"Total: {len(results)} | Passed: {passed} | Failed: {failed}")

    return failed


def check_user_status():
    response, _ = get_user(1)
    assert response.status_code == 200, f"Got {response.status_code}"


def check_user_json():
    response, _ = get_user(1)
    assert isinstance(response.json(), dict)


def check_user_fields():
    response, _ = get_user(1)
    user = response.json()
    assert user.get("id") == 1
    assert user.get("name")
    assert user.get("email")


def check_user_details():
    response, _ = get_user(1)
    user = response.json()
    assert isinstance(user.get("address"), dict)
    assert isinstance(user.get("company"), dict)


def check_missing_user():
    response, _ = get_user(9999)
    assert response.status_code == 404, f"Got {response.status_code}"


def check_posts_status():
    response, _ = get_posts()
    assert response.status_code == 200, f"Got {response.status_code}"


def check_posts_list():
    response, _ = get_posts()
    posts = response.json()
    assert isinstance(posts, list) and posts


def check_post_fields():
    response, _ = get_posts()
    post = response.json()[0]
    assert isinstance(post.get("id"), int)
    assert post.get("title")
    assert post.get("body")


def check_unique_post_ids():
    response, _ = get_posts()
    ids = [post["id"] for post in response.json()]
    assert len(ids) == len(set(ids))


def check_response_time():
    response, elapsed_ms = get_user(1)
    assert response.status_code == 200
    assert elapsed_ms >= 0


if __name__ == "__main__":
    failed = run_api_checks()
    raise SystemExit(1 if failed else 0)
