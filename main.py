import asyncio
from pathlib import Path
from typing import Any, Coroutine, Optional

import typer

import repo
from fetch import make_article
from render import Render

app = typer.Typer()


def run_async(coro: Coroutine) -> Any:
    return asyncio.get_event_loop().run_until_complete(coro)


@app.command("fetch")
def fetch(url: str):
    article = make_article(url)
    run_async(repo.save_article(article))
    typer.echo(f"Save Article {article.title}")


async def _render(title: str) -> Render:
    article = await repo.find_article(title)
    assert article
    return Render(article)


@app.command("render")
def render(title: str, out: Optional[str] = typer.Option(None)):
    typer.echo(f"Rendering {title}")
    md = run_async(_render(title))
    if out:
        Path(out).write_text(str(md), encoding="utf-8")
    else:
        typer.echo(md)


if __name__ == "__main__":
    app()
