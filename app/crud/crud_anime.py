from typing import Any, Dict, Union
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app import models, schemas
from app.schemas.anime import AnimeUpdate


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


def update_anime(db: Session, db_anime: models.Anime, obj_in: Union[AnimeUpdate, Dict[str, Any]]):
    obj_data = jsonable_encoder(db_anime)
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_anime, field, update_data[field])
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime


def remove_anime(db: Session, anime_id: int):
    db_anime = db.query(models.Anime).get(anime_id)
    db.delete(db_anime)
    db.commit()
    return db_anime
