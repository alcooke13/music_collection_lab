from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
# import repositories.album_repository as album_repository


def save(album):
    sql = """INSERT INTO albums (name, genre)
    VALUES (%s, %s) RETURNING *"""
    values = [album.name, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['name'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

# def select(id):
#     artist = None
#     sql = "SELECT * FROM artists WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)
#     if results:
#         result = results[0]
#         artist = Artist(result['name'])
#     return artist