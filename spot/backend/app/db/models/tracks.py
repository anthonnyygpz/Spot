from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.properties import ForeignKey
from spot.backend.app.db.database import Base


class Tracks(Base):
    __tablename__ = "tracks"

    id = Column(Integer(),nullable=True, primary_key=True, autoincrement=True)
    title = Column(String(),nullable=True)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    album_id = Column(Integer, ForeignKey('albums.id'))
    duration = Column(Integer(),nullable=True)
    file_path = Column(String(),nullable=True)
    s3_bucket_url = Column(String(),nullable=True)
    play_count = Column(Integer(), nullable=True)
