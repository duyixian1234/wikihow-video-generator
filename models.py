from dataclasses import dataclass, field


@dataclass
class Step:
    pic: str
    text: str


@dataclass
class Approach:
    name: str
    steps: list[Step] = field(default_factory=list)


@dataclass
class Article:
    _id: str
    title: str
    origin: str
    intro: str
    approaches: list[Approach] = field(default_factory=list)
