from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Artist, Album, Base
import random
import string

engine = create_engine('sqlite:///music.db', echo=True)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

session = Session()

for _ in range(100):
    name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 15)))
    artist = Artist(name=name)
    session.add(artist)

    for _ in range(random.randint(1, 5)):
        title = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 20)))
        album = Album(title=title, artist=artist)
        session.add(album)


session.commit()
session.close()