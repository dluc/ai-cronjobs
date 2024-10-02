import requests
from bs4 import BeautifulSoup


def get_content_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    return response.text


def get_text_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.get_text()
