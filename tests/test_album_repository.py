from lib.album_repository import AlbumRepository
from lib.album import Album
#from conftest import db_connection

"""
test, 1900, 1

When we call AlbumRepository # all
We get a list of Album objects reflecting the seed data.    
"""
def test_get_all_records(db_connection):
    # call all()  ---> all the entries
    db_connection.seed("seeds/music_library_addtable2.sql")
