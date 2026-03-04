import requests

class YouGileApi:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_new_project(self, title="New Test Project"):
        payload = {"title": title}

        response = requests.post(
            f"{self.base_url}/api-v2/projects",
            json=payload,
            headers=self.headers
        )

        assert response.status_code == 201, f"Ожидали 201, получили {
            response.status_code}"

        return response
