from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()
print(connection.DATABASE_NAME)

# Seed with some seed data
connection.seed("seeds/music_library.sql")
#connection.seed("seeds/music_library_addtable.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)
