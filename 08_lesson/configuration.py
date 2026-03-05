TOKEN = "CiycCq6hRNuo3ss+2-Qvr7r7fKOAc--GHxBE0qTUQMTyDv3hNyd95ckOsO7iY5mu"

BASE_URL = "https://ru.yougile.com"

AUTH_DATA = {
    "login": "dashakachalova6@gmail.com",
    "password": "mnb098890bnm",
    "companyId": "12838985-1a93-4600-a686-a5100e2e991c"
}

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

PROJECT_DATA = {
    "title": "Мой новый проект"
}

EMPTY_TITLE_PAYLOAD = {
    "title": ""
}

DELETE_PROJECT_PAYLOAD = {
    "deleted": True
}

BAD_HEADERS = {
    "Content-Type": "application/json"
}

DELETE_PROJECT_PAYLOAD = {
    "deleted": True
}

EXPECTED_PROJECT_TITLE = "New Test Project"

FAKE_ID = "1f324re4gae29frv-jlds-jn91d256ds23ijsasD"
