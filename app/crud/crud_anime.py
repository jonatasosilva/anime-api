from sqlalchemy.orm import Session
from app import models, schemas


def create_anime(db: Session, anime: schemas.AnimeCreate):
    db_anime = models.Anime(title=anime.title, description=anime.description)
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime


def get_anime(db: Session, anime_id: int):
    return db.query(models.Anime).filter(models.Anime.id == anime_id).first()


def get_animes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Anime).offset(skip).limit(limit).all()


def remove_anime(db: Session, anime_id: int):
    db_anime = db.query(models.Anime).get(anime_id)
    db.delete(db_anime)
    db.commit()
    return db_anime
