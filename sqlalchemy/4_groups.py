import sqlalchemy as db

engine = db.create_engine('sqlite:///chinook.db')
connection = engine.connect()
metadata = db.MetaData()

users = db.Table('customers', metadata, autoload_with=engine)

query = db.select(
    db.func.count(),
    users.columns.Company
).group_by(users.columns.Company)

print(query)
print()

resultProxy = connection.execute(query)
resultSet = resultProxy.fetchall()
print(resultSet)