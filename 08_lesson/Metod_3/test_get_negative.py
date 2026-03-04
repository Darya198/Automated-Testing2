import requests
from configuration import TOKEN


base_url = "https://ru.yougile.com"


def test_put_delete_negative_not_found():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    fake_id = "1f324re4gae29frv-jlds-jn9ld256ds23ijsasD"

    response = requests.get(
        f"{base_url}/api-v2/projects/{fake_id}", headers=headers)

    assert response.status_code == 404, f"Ожидали 404, получили {
        response.status_code}"
