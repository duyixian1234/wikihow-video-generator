import typer
from fetch import make_article
from repo import save_article
import asyncio

app = typer.Typer()


@app.command("fetch")
def fetch(url: str):
    article = make_article(url)
    asyncio.get_event_loop().run_until_complete(save_article(article))
    typer.echo(f"Save Article {article.title}")


@app.command("render")
def render(title: str):
    typer.echo(f"Rendering {title}")


if __name__ == "__main__":
    app()
