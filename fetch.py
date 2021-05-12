import requests
from bs4 import BeautifulSoup


def getHtml(url: str) -> str:
    resp = requests.get(url)
    return resp.text


def parse(content: str) -> BeautifulSoup:
    return BeautifulSoup(content, features="html.parser")
