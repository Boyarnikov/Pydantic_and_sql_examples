import sqlalchemy as db

engine = db.create_engine('sqlite:///chinook.db', echo=True)
connection = engine.connect()
metadata = db.MetaData()

users = db.Table('customers', metadata, autoload_with=engine)

print(users.columns.keys())
