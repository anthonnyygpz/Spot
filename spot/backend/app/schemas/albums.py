from typing import Optional
from pydantic import BaseModel


class AlbumsBase(BaseModel):
    artist_id: int
    title: str
    release_date: str
    cover_image: Optional[str]
    genre: str


class CreateAlbumsSchema(AlbumsBase):
    pass


class GetAlbumsSchema(AlbumsBase):
    pass
