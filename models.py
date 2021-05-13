from pydantic import BaseModel, Field


class Step(BaseModel):
    pic: str
    sub_steps: list[str]


class Approach(BaseModel):
    name: str
    steps: list[Step] = Field(default_factory=list)


class Article(BaseModel):
    id: str = Field(alias="_id")
    title: str
    origin: str
    intro: str
    approaches: list[Approach] = Field(default_factory=list)
