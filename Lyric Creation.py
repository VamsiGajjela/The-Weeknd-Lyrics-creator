#Vamsi Madhav Gajjela
#09/11/2019
from typing import List, Dict
import urllib.request
import random

def lyric_collecter(link) -> dict:
    """
    Gets all the lyrics from a song and returns a dictionary version of them
    """
    all_lyrics = []
    f = urllib.request.urlopen(link)
    sentence = b''
    text = b'<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->\r\n'
    for lines in f:
        if text in lines:
            while  b'</div>\r\n' not in sentence:
                sentence = f.readline()
                if b'[' not in sentence and b']' not in sentence and b'xe' not in sentence:
                    if str(sentence)[2:-7].replace('\\','').replace('<b>','') != '':
                        all_lyrics.append(str(sentence)[2:-7].replace('\\','').replace(')','').replace('<i>','').
                                          replace('<i>[English Translation: ','').replace('xe2x80x99','\'').\
                                          replace('<b>','').replace('&quot;','').replace('(','').replace('...',''))
            return all_lyrics[:-2]
    
        
def make_dictionary(lyrics) -> Dict[str, List[str]]:
    """
    Creates a dictionary with all the words in a given song
    """
    new = []
    all_words = {'': []}
    for values in range(len(lyrics)):  
        all_words[''] += [lyrics[values].split()[0]]

    for lines in lyrics:
        lines = lines.split()
        for word in range(len(lines) - 1):
            if lines[word] in all_words:
                all_words[lines[word]] += [lines[word + 1]]
            else:
                all_words[lines[word]] = [lines[word + 1]]
    return all_words
            

def artist_mimc(word_dict: Dict[str, List[str]]) -> str:
    """
    Goes through a dictionary of random words and formulates a sentece
    based on usage in the song
    """
    current_word = ''
    sentence = ''
    for counter in range(1000):
        try:
            current_word = random.choice(word_dict[current_word])
        except KeyError:
            return sentence
        sentence += current_word + ' '


def song_maker(word_dict, num_of_line):
    """
    Creates a random song based on common sentence structure and word usage
    """
    song = ''
    for sentence in range(num_of_line):
        song += str(artist_mimc(word_dict)) + '\n'
    return song

song1 = 'https://www.azlyrics.com/lyrics/weeknd/starboy.html'
song2 = 'https://www.azlyrics.com/lyrics/weeknd/thehills.html'
song3 = 'https://www.azlyrics.com/lyrics/weeknd/wickedgames.html'
song4 = 'https://www.azlyrics.com/lyrics/danielcaesar/streetcar.html'
song5 = 'https://www.azlyrics.com/lyrics/weeknd/truecolors.html'
song6 = 'https://www.azlyrics.com/lyrics/weeknd/dieforyou.html'


all_songs = (song1, song2, song3, song4, song5, song6)

vocab = {}

for song in all_songs:
    lyrics = lyric_collecter(song)
    local_vocab = (make_dictionary(lyrics))
    for k in local_vocab:
        if k in vocab:
            vocab[k] += local_vocab[k]
        else:
            vocab[k] = local_vocab[k]
    
while True:
    choice = input('Hit enter to generate a song like The Weeknd: ')
    if choice == '':
        len_of_song = int(input('How many lines would you like the line to be: '))
        print('\n' + song_maker(vocab, len_of_song) + '-' * 50)
    else:
        break
            
