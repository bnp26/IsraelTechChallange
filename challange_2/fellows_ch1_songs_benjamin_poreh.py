from random import Random

class Song:
    def __init__(self):
        self.name = ""
        
class Playlist:
    def __init__(self, passed_songs):
        if passed_songs == None:
            self.songs = dict()
        else:
            self.songs = passed_songs
            
    def gen_rand_playlist(self):
        randomized = dict()
        for song in self.songs:
            ran_num = Random.random()
            randomized[ran_num] = song
            key_list = randomized.keys()
            length = len(randomized)
            
def find_loc (key_num_list, rand, pivot):
    if rand > key_num_list[pivot]:
        return find_loc(key_num_list, rand, pivot*1.5)
    elif rand < key_num_list[pivot]:
        return find_loc(key_num_list, rand, pivot/1.5)
    else:
        return pivot


def main():
    songs = {1:Song("BabyGotBack"), 2:Song("TwoStep"), 3:Song("ShitFuckStack"), 4:Song("EnormousPenis")}
    playlist = Playlist(songs)
    print str(playlist.gen_rand_playlist())
    
    
    
    
    