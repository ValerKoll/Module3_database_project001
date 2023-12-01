from lib.album import Album

"""
constructs with an id, title and year, album
"""
def test_album_constructs():
    album = Album(1, "Album1", 1990, 1)
    assert album.title == "Album1"
    assert album.release_year == 1990
    assert album.artist_id == 1

"""
We can format album to strings nicely
"""
def test_artists_format_nicely():
    album = Album(1, "Album1", 1990, 1)
    assert str(album) == "Album(1, Album1, 1990, 1)"


"""
We can compare two identical albums
And have them be equal
"""
def test_artists_are_equal():
    album1 = Album(1, "Album1", 1990, 1)
    album2 = Album(1, "Album1", 1990, 1)
    assert album1 == album2

