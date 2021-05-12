from playwright.async_api import async_playwright
import asyncio
from pathlib import Path


async def main():

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            headless=False,
        )
        page = await browser.new_page(viewport=dict(width=1920, height=1080))
        await page.goto(
            "https://zh.wikihow.com/%E6%89%93%E8%B4%A5%E5%91%A8%E4%B8%80%E6%97%A9%E6%99%A8%E5%BF%A7%E9%83%81%E7%97%87",
            wait_until="domcontentloaded",
        )
        section = 0
        while element := await page.query_selector(f"#mf-section-{section}"):
            print(f"{section=}")
            if not section:
                await element.screenshot(path=f"section-{section}.png")
                text = await element.inner_text()
                Path(f"section-{section}.txt").write_text(text)
                section += 1
                continue
            step_index = 1
            while step := await element.query_selector(f".step-id-{step_index:02}"):
                await step.screenshot(path=f"{section}-{step_index}.png")
                text = await step.inner_text()
                Path(f"{section}-{step_index}.txt").write_text(text)
                step_index += 1
            section += 1
        await browser.close()


asyncio.run(main())
