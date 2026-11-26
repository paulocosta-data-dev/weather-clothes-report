import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def fetch_json(url):

    retry = Retry(
        total=3,
        connect=3,
        read=3,
        status=3,
        backoff_factor=1,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"})
    )

    with requests.Session() as session:

        session.mount(
            "https://",
            HTTPAdapter(max_retries=retry)
        )

        response = session.get(
            url,
            timeout=(20, 30)
        )

        response.raise_for_status()

        return response.json()