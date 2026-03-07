import requests
from configuration import TOKEN, BASE_URL, EXPECTED_PROJECT_TITLE
from yougile_api import YouGileApi

api = YouGileApi("https://ru.yougile.com", TOKEN)


def test_put_delete_positive():
    response = api.create_new_project()

    project_id = response.json()['id']

    url = f"{BASE_URL}/projects/{project_id}"

    get_response = requests.get(url, headers=api.headers)

    assert get_response.status_code == 200, f"Ожидали 200, получили {
        get_response.status_code}"

    assert get_response.json()["title"] == EXPECTED_PROJECT_TITLE
    assert get_response.json()["id"] == project_id
