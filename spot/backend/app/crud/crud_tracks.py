from dataclasses import dataclass

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from spot.backend.app.db.models.artists import Artists

from ..schemas.tracks import CreateTracksSchema
from ..db.models.tracks import Tracks

@dataclass
class TracksDB:
    db: Session

    def create_tracks(self,track: CreateTracksSchema, duration: int, url: str):
        try:
            db_track = Tracks(**track.model_dump(exclude={"location_url"}), s3_bucket_url=url, duration= duration)  
            self.db.add(db_track)
            self.db.commit()
            self.db.refresh(db_track)
            return db_track
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_tracks(self, skip: int, limit:int):
        try:
            db_track = self.db.query(Tracks, Tracks.title, Artists.name, Tracks.file_path, Tracks.s3_bucket_url).join(Tracks.artist).all() 
            return [
                {'title': track.title, 'name': track.name, 'image': track.file_path, 's3_bucket_url': track.s3_bucket_url}
                for track in db_track
            ] 
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_info_tracks(self, track_id:int ):
        try:
            db_track = self.db.query(Tracks).filter(Tracks.id == track_id).first() 
            return db_track
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
