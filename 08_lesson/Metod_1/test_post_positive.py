from configuration import BASE_URL, HEADERS, PROJECT_DATA
from yougile_api import YouGileApi

api = YouGileApi(BASE_URL, HEADERS)


def test_post_positive():
    response = api.create_new_project(PROJECT_DATA)

    body = response.json()
    assert "id" in body
    print(f"Успех! ID: {body['id']}")
