from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ...db.database import Base


class Albums(Base):
    __tablename__ = "albums"

    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    title = Column(String(), nullable=True)
    release_date = Column(DateTime(timezone=True), nullable=False, default=func.now())
    cover_image = Column(String(), nullable=True)
    genre = Column(String(), nullable=True)

    tracks = relationship("Tracks", backref="album")
