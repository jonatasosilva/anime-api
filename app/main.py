from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/animes/", response_model=schemas.Anime)
def create_anime(anime: schemas.Anime, db: Session = Depends(get_db)):
    return crud.create_anime(db=db, anime=anime)


@app.get("/animes/{anime_id}", response_model=schemas.Anime)
def read_anime(anime_id: int, db: Session = Depends(get_db)):
    db_anime = crud.get_anime(db, anime_id=anime_id)
    if db_anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    return db_anime
