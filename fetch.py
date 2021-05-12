import requests
from bs4 import BeautifulSoup

from models import Approach, Article, Step


def getHtml(url: str) -> str:
    resp = requests.get(url)
    return resp.text


def parse(content: str) -> BeautifulSoup:
    return BeautifulSoup(content, features="html.parser")


def make_article(url: str) -> Article:
    raw = getHtml(url)
    html = parse(raw)
    main = html.select_one(".mw-parser-output")
    intro = make_intro(main.select_one("#intro").select_one("#mf-section-0"))
    article = Article(
        title=html.title.text, _id=html.title.text, origin=url, intro=intro
    )
    approaches = [make_approach(step) for step in main.select(".steps")]
    article.approaches = approaches
    return article


def make_intro(intro):
    ret = ""
    for child in intro:
        if child.name != "sup":
            ret += child.text if child.name else child
    return ret


def make_approach(step):
    name = step.select_one(".mw-headline")
    approach = Approach(name=name.text)
    steps = [make_step(section) for section in step.select(".section_text")]
    approach.steps = steps
    return approach


def make_step(section):
    img = section.select_one("img").get("data-srclarge")
    step = Step(pic=img, text="")
    for sub_step in section.select(".step"):
        for child in sub_step.children:
            if child.name != "sup":
                content = child.text if child.name else child
                if content:
                    step.text += content
    return step
