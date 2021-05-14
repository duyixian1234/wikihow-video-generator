from pydantic import BaseModel, Field


class Step(BaseModel):
    pic: str
    sub_steps: list[str]

    def full_text(self):
        return "\n".join(self.sub_steps)


class Approach(BaseModel):
    name: str
    steps: list[Step] = Field(default_factory=list)

    def full_text(self):
        text = self.name
        text += "\n" + "---" + "\n"
        text += "\n".join(step.full_text() for step in self.steps)
        return text


class Article(BaseModel):
    id: str = Field(alias="_id")
    title: str
    origin: str
    intro: str
    approaches: list[Approach] = Field(default_factory=list)

    def full_text(self):
        text = self.title
        text += "\n" + "---"
        text += "\n" + self.intro
        text += "\n" + "---" + "\n"
        text += "\n".join(approach.full_text() for approach in self.approaches)
        return text
