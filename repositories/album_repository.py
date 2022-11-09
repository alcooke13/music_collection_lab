# from db.run_sql import run_sql
# from models.artist import Artist
# import repositories.artist_repository as artist_repository


# def save(album):
#     sql = """INSERT INTO albums (name, genre)
#     VALUES (%s, %s) RETURNING *"""
#     values = [album.name, album.genre]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     album.id = id
#     return album