import requests
from configuration import TOKEN


base_url = "https://ru.yougile.com"


def test_post_negative_empty_title():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "title": ""
    }

    response = requests.post(
        base_url + "/api-v2/projects", json=payload, headers=headers)

    assert response.status_code == 400
