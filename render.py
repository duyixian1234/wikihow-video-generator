from typing import List

from models import Approach, Article, Step

MARP = """---
marp: true
theme: gaia
paginate: true
---"""


class Render:
    def __init__(self, article: Article):
        self.article = article
        self.md: List[str] = []
        (
            self.add_marp()
            .add_title()
            .add_intro()
            .add_approaches()
            .add_tips()
            .add_warnings()
            .add_ending()
        )

    def add_marp(self) -> "Render":
        self.md.append(MARP)
        return self

    def add_title(self) -> "Render":
        self.md.append(f"# {self.article.title}")
        return self.add_description().add_split()

    def add_description(self) -> "Render":
        self.md.append(f"原文：[{self.article.origin}]({self.article.origin})")
        return self

    def add_split(self) -> "Render":
        self.md.append("\n---\n")
        return self

    def add_intro(self) -> "Render":
        self.md.append(f"{self.article.intro}")
        return self.add_split()

    def add_approaches(self) -> "Render":
        for approach in self.article.approaches:
            self.add_approach(approach)
        return self

    def add_approach(self, approach: Approach) -> "Render":
        self.md.append(f"## {approach.name}")
        self.add_split()
        for step in approach.steps:
            self.add_step(step)
        return self

    def add_step(self, step: Step) -> "Render":
        if step.pic:
            self.md.append(f"![]({step.pic})")
            self.add_split()
        for sub_step in step.sub_steps:
            self.md.append(sub_step)
            self.add_split()
        return self

    def add_tips(self) -> "Render":
        if not self.article.tips:
            return self
        self.md.append("## 小提示")
        self.md.extend(self.article.tips)
        self.add_split()
        return self

    def add_warnings(self) -> "Render":
        if not self.article.warnings:
            return self
        self.md.append("## 警告")
        self.md.extend(self.article.warnings)
        self.add_split()
        return self

    def add_ending(self) -> "Render":
        self.md.append("## 感谢观看")
        return self

    def __str__(self):
        return "\n".join(self.md)
