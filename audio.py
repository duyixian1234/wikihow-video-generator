from pathlib import Path

import repo
import transform
import utils


async def make_audio(title: str):
    article = await repo.find_article(title)
    assert article
    text = article.full_text()
    index = 0
    empty = Path("3s.mp3").read_bytes()
    for paragraph in text.split("\n"):
        if not paragraph:
            continue
        for sentence in utils.tokenize(paragraph):
            path = Path("audio") / f"{index:03}.mp3"
            audio = empty if sentence == "---" else transform.transform(sentence)
            path.write_bytes(audio)
            print(f"Save {path}")
            index += 1
