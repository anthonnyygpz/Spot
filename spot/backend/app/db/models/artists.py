from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class Artists(Base):
    __tablename__ = "artists"

    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    bio = Column(String(), nullable=True)
    profile_picture = Column(String(), nullable=True)
    monthly_listeners = Column(Integer(), nullable=False)

    albums = relationship("Albums", backref="artist")
    tracks = relationship("Tracks", backref="artist")
