import asyncio
from dataclasses import asdict

from motor.motor_asyncio import AsyncIOMotorClient

from models import Article

client = AsyncIOMotorClient(
    "mongodb://127.0.0.1:27017/wikihow", io_loop=asyncio.get_event_loop()
)
db = client.get_default_database()


async def saveArticle(article: Article) -> None:
    await db.articles.insert_one(asdict(article))
