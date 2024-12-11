from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..schemas.artists import CreateArtistsSchema
from ..crud.crud_artists import ArtistsDB


class ArtitsRepositories:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_artists(self, artist: CreateArtistsSchema):
        try:
            # s3_client.upload_file(artist.file_path, bucket_name, artist.title)
            return ArtistsDB(self.db).create_artists(artist)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

    def get_artists(self, skip: int, limit: int):
        try:
            return ArtistsDB(self.db).get_artists(skip, limit)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

    def get_info_artists(self, artists_id: int):
        try:
            return ArtistsDB(self.db).get_info_artists(artists_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
