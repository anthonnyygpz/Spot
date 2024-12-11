from pydantic import BaseModel


class TracksBase(BaseModel):
    title: str
    artist_id: int
    album_id: int
    file_path: str
    play_count: int

    
class CreateTracksSchema(TracksBase):
    location_url: str

class GetTracksSchema(TracksBase):
    id: int
    s3_bucket_url: str
    duration: int
    pass

