from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.crud import crud_anime
from app.dependencies import get_db


router = APIRouter()


@router.post("/animes/", response_model=schemas.Anime)
def create_anime(anime: schemas.Anime, db: Session = Depends(get_db)):
    return crud_anime.create_anime(db=db, anime=anime)


@router.get("/animes/{anime_id}", response_model=schemas.Anime)
def read_anime(anime_id: int, db: Session = Depends(get_db)):
    db_anime = crud_anime.get_anime(db, anime_id=anime_id)
    if db_anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    return db_anime


@router.get("/animes/", response_model=List[schemas.Anime])
def read_animes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    animes = crud_anime.get_animes(db, skip=skip, limit=limit)
    return animes


@router.put("/animes/{anime_id}", response_model=schemas.Anime)
def update_item(anime_id: int, anime_in: schemas.AnimeUpdate, db: Session = Depends(get_db)):
    anime = crud_anime.get_anime(db=db, anime_id=anime_id)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    anime = crud_anime.update_anime(db=db, db_anime=anime, obj_in=anime_in)
    return anime


@router.delete("/animes/{anime_id}", response_model=schemas.Anime)
def delete_anime(anime_id: int, db: Session = Depends(get_db)):
    anime = crud_anime.get_anime(db, anime_id=anime_id)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return crud_anime.remove_anime(db, anime_id=anime_id)
