from pydantic import BaseModel


class AnimeBase(BaseModel):
    title: str
    description: str


class AnimeCreate(AnimeBase):
    pass


class Anime(AnimeBase):
    id: int = None

    class Config:
        orm_mode = True
