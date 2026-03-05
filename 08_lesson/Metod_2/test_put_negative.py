import requests
from configuration import BASE_URL, TOKEN, BAD_HEADERS, DELETE_PROJECT_PAYLOAD
from yougile_api import YouGileApi

api = YouGileApi(BASE_URL, TOKEN)


def test_put_delete_negative_unauthorized():
    response = api.create_new_project()

    project_id = response.json()['id']

    url = f"{BASE_URL}/api-v2/projects/{project_id}"

    response = requests.put(
        url, json=DELETE_PROJECT_PAYLOAD,
        headers=BAD_HEADERS
        )

    assert response.status_code == 401, f"Ожидали 401, получили {
        response.status_code}"
