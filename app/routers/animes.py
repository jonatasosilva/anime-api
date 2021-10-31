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
