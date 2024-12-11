from fastapi import HTTPException
from sqlalchemy.orm import Session


from ..crud.crud_albums import AlbumsDB
from ..schemas.albums import CreateAlbumsSchema


class AlbumsRepositories:
    def __init__(self, db: Session):
        self.db = db

    def create_albums(self, album: CreateAlbumsSchema):
        try:
            return AlbumsDB(self.db).create_albums(album)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_albums(self, skip: int, limit: int):
        try:
            return AlbumsDB(self.db).get_albums(skip, limit)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_info_albums(self, artist_id: int):
        try:
            return AlbumsDB(self.db).get_info_albums(artist_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
