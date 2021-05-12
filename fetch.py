from playwright.async_api import async_playwright, Page, ElementHandle
import asyncio
from models import Article, Method, Step


async def getIntro(page: Page):
    element = await page.query_selector(f"#mf-section-0")
    assert element
    return await element.inner_text()


async def getName(method: ElementHandle):
    element = await method.query_selector(".mw-headline")
    if not element:
        return ""
    return await element.inner_text()


async def generateMethods(page: Page):
    section = 1
    while element := await page.query_selector(f"#mf-section-{section}"):
        yield element
        section += 1


async def generateSteps(section: ElementHandle):
    step = 1
    while element := await section.query_selector(f"#step-id-{step:02}"):
        url = ""
        if img := await element.query_selector(".image"):
            url = await img.get_attribute("href")
        text = await element.inner_text()
        yield url, text
        step += 1


async def fetch(url: str):

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            headless=False,
        )
        page = await browser.new_page(viewport=dict(width=1920, height=1080))
        await page.goto(
            url,
            wait_until="domcontentloaded",
        )
        intro = await getIntro(page)
        article = Article(title="aaa", origin=url, intro=intro)
        async for method in generateMethods(page):
            name = await getName(method)
            if not name:
                continue
            new = Method(name=name)
            async for url, text in generateSteps(method):
                new.steps.append(Step(pic=url, text=text))
            article.methods.append(new)
        print(article)
        await browser.close()


asyncio.run(
    fetch(
        "https://zh.wikihow.com/%E6%89%93%E8%B4%A5%E5%91%A8%E4%B8%80%E6%97%A9%E6%99%A8%E5%BF%A7%E9%83%81%E7%97%87"
    )
)
