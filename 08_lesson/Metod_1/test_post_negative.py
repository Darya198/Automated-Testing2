import requests
from configuration import BASE_URL, HEADERS, EMPTY_TITLE_PAYLOAD


def test_post_negative_empty_title():
    url = f"{BASE_URL}/api-v2/projects"

    response = requests.post(
        url, json=EMPTY_TITLE_PAYLOAD, headers=HEADERS)

    assert response.status_code == 400
