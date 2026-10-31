
import pytest
from api_client import get_user, get_posts


def test_user_status_code():
    response, _ = get_user(1)
    assert response.status_code == 200


def test_user_valid_json():
    response, _ = get_user(1)
    user = response.json()
    assert isinstance(user, dict)


def test_user_has_required_fields():
    response, _ = get_user(1)
    user = response.json()
    assert user["id"] == 1
    assert isinstance(user["name"], str) and user["name"]
    assert isinstance(user["email"], str) and user["email"]


def test_user_address_and_company():
    response, _ = get_user(1)
    user = response.json()
    assert isinstance(user["address"], dict)
    assert isinstance(user["company"], dict)


def test_missing_user_returns_not_found():
    response, _ = get_user(9999)
    assert response.status_code == 404


def test_posts_status_code():
    response, _ = get_posts()
    assert response.status_code == 200


def test_posts_are_a_nonempty_list():
    response, _ = get_posts()
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0


def test_post_has_required_fields():
    response, _ = get_posts()
    posts = response.json()
    assert isinstance(posts[0]["id"], int)
    assert posts[0]["title"]
    assert posts[0]["body"]


def test_post_ids_are_unique():
    response, _ = get_posts()
    posts = response.json()
    ids = [post["id"] for post in posts]
    assert len(ids) == len(set(ids))


def test_response_time_is_measured():
    response, elapsed_ms = get_user(1)
    assert response.status_code == 200
    assert elapsed_ms >= 0
