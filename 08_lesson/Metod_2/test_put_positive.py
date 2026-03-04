import requests
from configuration import TOKEN
from yougile_api import YouGileApi

api = YouGileApi("https://ru.yougile.com", TOKEN)


def test_put_delete_positive():
    response = api.create_new_project()

    body = response.json()
    assert "id" in body
    project_id = body['id']

    delete_payload = {
        "deleted": True
    }

    delete_response = requests.put(
        f"https://ru.yougile.com/api-v2/projects/{project_id}",
        json=delete_payload, headers=api.headers
        )

    assert delete_response.status_code == 200
    assert "id" in response.json()
