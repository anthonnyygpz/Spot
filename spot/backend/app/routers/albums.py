from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from spot.backend.app.dependencies import get_db
from spot.backend.app.services.albums import AlbumsRepositories
from ..schemas.albums import CreateAlbumsSchema

router = APIRouter(
    prefix="/api",
    tags=["albums"],
    responses={
        400: {"description": "Not found"},
    },
)


@router.post("/create_albums")
async def create_albums(album: CreateAlbumsSchema, db: Session = Depends(get_db)):
    return AlbumsRepositories(db).create_albums(album)


@router.get("/get_albums")
async def get_albums(skip: int = 1, limit: int = 100, db: Session = Depends(get_db)):
    return AlbumsRepositories(db).get_albums(skip, limit)


@router.get("/get_info_albums")
async def get_info_albums(artist_id: int, db: Session = Depends(get_db)):
    return AlbumsRepositories(db).get_info_albums(artist_id)
