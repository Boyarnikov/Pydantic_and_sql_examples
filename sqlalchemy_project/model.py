from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    albums = relationship('Album', backref='artist')

    def __repr__(self):
        return f"Artist(id={self.id}, name='{self.name}')"

# Define the Album model
class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey('artists.id'))

    def __repr__(self):
        return f"Album(id={self.id}, title='{self.title}', artist_id={self.artist_id})"