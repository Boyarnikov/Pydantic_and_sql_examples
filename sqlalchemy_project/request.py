from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import sessionmaker, relationship
from model import Album, Artist


engine = create_engine('sqlite:///music.db', echo=True)

Session = sessionmaker(bind=engine)

with sessionmaker(bind=engine)() as session:
    results = session.query(
        Artist.name,
        func.count(Album.id).label('album_count')
    ).outerjoin(Album).group_by(Artist.id).all()

    print(results)

    for artist_name, album_count in results:
        print(f"Artist: {artist_name}, Album Count: {album_count}")
        