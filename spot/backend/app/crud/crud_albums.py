from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..db.models.albums import Albums
from ..schemas.albums import CreateAlbumsSchema


class AlbumsDB:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_albums(self, album: CreateAlbumsSchema):
        try:
            db_album = Albums(**album.model_dump(exclude={"release_date"}))
            self.db.add(db_album)
            self.db.commit()
            self.db.refresh(db_album)

            return db_album
        except HTTPException as he:
            raise HTTPException(status_code=400, detail=str(he))
        except Exception as e:
            self.db.rollback()  # Hacemos rollback en caso de error
            raise HTTPException(status_code=500, detail=str(e))

    def get_albums(self, skip: int, limit: int):
        try:
            db_album = self.db.query(Albums).offset(skip - 1).limit(limit).all()
            return db_album
        except HTTPException as he:
            raise HTTPException(status_code=400, detail=str(he))
        except Exception as e:
            self.db.rollback()  # Hacemos rollback en caso de error
            raise HTTPException(status_code=500, detail=str(e))

    def get_info_albums(self, artists_id: int):
        try:
            db_album = (
                self.db.query(Albums).filter(Albums.artist_id == artists_id).first()
            )
            return db_album
        except HTTPException as he:
            raise HTTPException(status_code=400, detail=str(he))
        except Exception as e:
            self.db.rollback()  # Hacemos rollback en caso de
            raise HTTPException(status_code=500, detail=str(e))
