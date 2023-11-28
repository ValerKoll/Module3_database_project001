from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# result = connection.execute("SELECT * FROM albums;")
# for i in result:
#     print(i['id'], i['title'])
