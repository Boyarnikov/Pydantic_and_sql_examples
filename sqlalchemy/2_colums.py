import sqlalchemy as db

engine = db.create_engine('sqlite:///chinook.db')
connection = engine.connect()
metadata = db.MetaData()

users = db.Table('customers', metadata, autoload_with=engine)

query = db.select(users.columns.FirstName, users.columns.LastName)
print(query)
print()

resultProxy = connection.execute(query)
resultSet = resultProxy.fetchall()
print(resultSet)