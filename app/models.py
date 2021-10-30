from sqlalchemy import Column, Integer, String

from .database import Base


class Anime(Base):
    __tablename__ = "animes"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
