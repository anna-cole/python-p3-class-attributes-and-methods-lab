class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre in cls.genres:
            None  
        else: 
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1 

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
# teen_spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
# you_could_be_mine = Song("You Could Be Mine", "Guns N'Roses", "Rock")
# rape_me = Song("Rape Me", "Nirvana", "Rock")
# print(ninety_nine_problems.name)
# print(ninety_nine_problems.artist)
# print(ninety_nine_problems.genre)
# print(Song.count)
# print(Song.genres)
# print(Song.artists)
# print(Song.genre_count)
# print(Song.artist_count)



