class Song:
    coount = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        if genre not in Song.genres:
            Song.genres.append(genre)
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1
        if artist not in Song.artists:
            Song.artists.append(artist)
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1
    def __str__(self):
        return f"{self.name} by {self.artist} ({self.genre})"
    def __repr__(self):
        return f"Song({self.name}, {self.artist}, {self.genre})"
    def __eq__(self, other):
        return self.name == other.name and self.artist == other.artist and self.genre == other.genre
    def __ne__(self, other):
        return not self.__eq__(other)
    
    pass
