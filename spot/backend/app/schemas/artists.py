from typing import Optional
from pydantic import BaseModel


class ArtistsBase(BaseModel):
    name: str
    bio: str
    monthly_listeners: int


class CreateArtistsSchema(ArtistsBase):
    profile_picture: Optional[str]


class GetArtistsSchema(ArtistsBase):
    id: int
    profile_picture: Optional[str]
