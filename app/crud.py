from sqlalchemy.orm import Session

from . import models, schemas


def get_anime(db: Session, anime_id: int):
    return db.query(models.Anime).filter(models.Anime.id == anime_id).first()


def create_anime(db: Session, anime: schemas.AnimeCreate):
    db_anime = models.Anime(title=anime.title, description=anime.description)
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime
