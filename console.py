import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Oasis')
artist_repository.save(artist_1)

artist_2 = Artist('BTS')
artist_repository.save(artist_2)

album_1 = Album("Roll With It", "Rock", artist_1)
album_repository.save(album_1)
album_2 = Album("Another Album", "Pop", artist_1)
album_repository.save(album_2)

# album_1.genre = "Pop"
# album_repository.update(album_1)
result = artist_repository.select_all()

# # result = artist_repository.select_all()
# result = album_repository.select_all()
# # artist_repository.delete(1)

# for album in result:
#      print(album.__dict__) 

# select_artist = artist_repository.select(22)
# print (select_artist)


pdb.set_trace()
