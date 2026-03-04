import requests
from configuration import TOKEN
from yougile_api import YouGileApi

api = YouGileApi("https://ru.yougile.com", TOKEN)


def test_put_delete_positive():
    response = api.create_new_project()

    body = response.json()
    assert "id" in body
    project_id = body['id']

    get_response = requests.get(
        f"https://ru.yougile.com/api-v2/projects/{project_id}",
        headers=api.headers)

    assert get_response.status_code == 200, f"Ожидали 200, получили {
        get_response.status_code}"

    assert get_response.json()["title"] == "New Test Project"
    assert get_response.json()["id"] == project_id
