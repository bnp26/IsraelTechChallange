import random

#class Song so as to remember the songs name
#Song only has a string in it.
class Song:
    def __init__(self):
        self.name = ""

    def __init__(self, put_name):
	self.name = put_name

    def __repr__(self):
	return self.name
#class Playlist
#allows you to put songs into the playlist via constructor
#run gen_rand_playlist to generate a randomized playlist
class Playlist:
    def __init__(self, passed_songs):
        if passed_songs == None:
            self.songs = dict()
        else:
            self.songs = passed_songs
    
    def __repr__(self):
	return str(self.songs.values())

    def gen_rand_playlist(self):
        randomized = dict()
        size = len(self.songs)
	for song in self.songs:
            ran_num = random.random()
	    new_index = int(ran_num * 100)
	    randomized.setdefault(new_index, []).append(song)
	return randomized.values()

#to test, add songs in the style of {1:Song("Song Name"), 2:Song("Next Song"), 3:Song("Etc.")}
def main():
    songs = {1:Song("BabyGotBack"), 2:Song("TwoStep"), 3:Song("ShitFuckStack"), 4:Song("EnormousPenis")}
    playlist = Playlist(songs)
    final = playlist.gen_rand_playlist()
    print final

if __name__ == "__main__":
    main()
