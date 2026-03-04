import requests
from configuration import TOKEN
from yougile_api import YouGileApi

api = YouGileApi("https://ru.yougile.com", TOKEN)


def test_put_delete_negative_unauthorized():
    response = api.create_new_project()

    body = response.json()
    assert "id" in body
    project_id = body['id']

    bad_headers = {
        "Content-Type": "application/json"
        }

    payload = {
        "deleted": True
        }

    response = requests.put(
        f"https://ru.yougile.com/api-v2/projects/{project_id}",
        json=payload, headers=bad_headers
        )

    assert response.status_code == 401, f"Ожидали 401, получили {
        response.status_code}"
