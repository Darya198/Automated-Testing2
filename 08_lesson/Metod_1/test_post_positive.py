from configuration import TOKEN
from yougile_api import YouGileApi

api = YouGileApi("https://ru.yougile.com", TOKEN)


def test_post_positive():
    response = api.create_new_project()

    body = response.json()
    assert "id" in body
    print(f"Успех! ID: {body['id']}")
