import requests
from configuration import BASE_URL, HEADERS, FAKE_ID


def test_put_delete_negative_not_found():
    url = f"{BASE_URL}/api-v2/projects/{FAKE_ID}"

    response = requests.get(
        url, headers=HEADERS)

    assert response.status_code == 404, f"Ожидали 404, получили {
        response.status_code}"
