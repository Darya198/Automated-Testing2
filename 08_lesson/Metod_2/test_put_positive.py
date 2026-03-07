import requests
from configuration import TOKEN, BASE_URL, DELETE_PROJECT_PAYLOAD
from yougile_api import YouGileApi

api = YouGileApi(BASE_URL, TOKEN)


def test_put_delete_positive():
    response = api.create_new_project()

    project_id = response.json()['id']

    url = f"{BASE_URL}//api-v2/projects/{project_id}"

    delete_response = requests.put(
        url, json=DELETE_PROJECT_PAYLOAD,
        headers=api.headers
        )

    assert delete_response.status_code == 200
    assert "id" in delete_response.json()
