import asyncio
from dataclasses import asdict
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient

from models import Article

client = AsyncIOMotorClient(
    "mongodb://127.0.0.1:27017/wikihow", io_loop=asyncio.get_event_loop()
)
db = client.get_default_database()


async def save_article(article: Article) -> None:
    await db.articles.insert_one(article.dict(by_alias=True))


async def find_article(title: str) -> Optional[Article]:
    raw = await db.articles.find_one({"_id": title})
    return raw and Article.parse_obj(raw)
