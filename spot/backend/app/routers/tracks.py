from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas.tracks import CreateTracksSchema,GetTracksSchema

from ..dependencies import get_db
from ..services.tracks import TracksRepositories

router = APIRouter(prefix="/api",tags=["tracks"],responses={400: {"description":"Not found"}})

@router.post("/create_tracks")
async def create_tracks(track: CreateTracksSchema,db: Session = Depends(get_db)):
    return TracksRepositories(db).create_tracks(track)

@router.get("/get_tracks")
async def get_tracks(skip: int= 1, limit:int = 100,db: Session= Depends(get_db)):
    return TracksRepositories(db).get_tracks(skip, limit)

@router.get("/get_info_tracks")
async def get_info_trackas(track_id: int,db:Session = Depends(get_db)):
    return TracksRepositories(db).get_info_tracks(track_id)
