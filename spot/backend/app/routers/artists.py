from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from spot.backend.app.dependencies import get_db
from ..services.artists import ArtitsRepositories
from ..schemas.artists import CreateArtistsSchema

router = APIRouter(
    prefix="/api", tags=["artist"], responses={400: {"description": "Not found"}}
)


@router.post("/create_artists")
async def create_artists(artist: CreateArtistsSchema, db: Session = Depends(get_db)):
    return ArtitsRepositories(db).create_artists(artist)


@router.get("/get_artits")
async def get_artists(skip: int = 1, limit: int = 100, db: Session = Depends(get_db)):
    return ArtitsRepositories(db).get_artists(skip, limit)


@router.get("/get_info_artits")
async def get_info_artists(artists_id: int, db: Session = Depends(get_db)):
    return ArtitsRepositories(db).get_info_artists(artists_id)
