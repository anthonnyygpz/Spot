from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..schemas.artists import CreateArtistsSchema
from ..db.models.artists import Artists


class ArtistsDB:
    def __init__(self, db: Session):
        self.db = db

    def create_artists(self, artist: CreateArtistsSchema):
        try:
            db_artists = Artists(**artist.model_dump())
            self.db.add(db_artists)
            self.db.commit()
            self.db.refresh(db_artists)
            return db_artists
        except HTTPException as he:
            raise HTTPException(status_code=400, detail=str(he))
        except Exception as e:
            self.db.rollback()  # Hacemos rollback en caso de error
            raise HTTPException(status_code=500, detail=str(e))

    def get_artists(self, skip: int, limit: int):
        try:
            db_artists = self.db.query(Artists).offset(skip - 1).limit(limit).all()
            return db_artists
        except HTTPException as he:
            raise HTTPException(status_code=400, detail=str(he))
        except Exception as e:
            self.db.rollback()  # Hacemos rollback en caso de error
            raise HTTPException(status_code=500, detail=str(e))

    def get_info_artists(self, artists_id: int):
        try:
            db_artists = self.db.query(Artists).filter(Artists.id == artists_id).first()
            return db_artists
        except HTTPException as he:
            raise HTTPException(status_code=400, detail=str(he))
        except Exception as e:
            self.db.rollback()  # Hacemos rollback en caso de error
            raise HTTPException(status_code=500, detail=str(e))
