import sqlalchemy as db

engine = db.create_engine('sqlite:///chinook.db')
connection = engine.connect()
metadata = db.MetaData()

users = db.Table('customers', metadata, autoload_with=engine)

print(
    type(users.columns.Company),
    [tag for tag in dir(users.columns.Company) if not tag.startswith("_")]
)
query = db.select(
    users.columns.FirstName,
    users.columns.LastName,
    users.columns.Company
).where(users.columns.Company.is_not(None))

print(query)
print()

resultProxy = connection.execute(query)
resultSet = resultProxy.fetchall()
print(resultSet)