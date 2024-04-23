import sys
import argparse
import csv
import pandas as pd 

songs_csv = r'songs_normalize.csv'

with open(songs_csv, encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    
    genre_song_dict = {}
    genre_set = set()

# this loop creates a set of genre names
    for record in reader:

        record_genre = record['genre']
    
        for single_genre in record_genre.split(', '):
            genre_set.add(single_genre)


    for genre in genre_set:
        songs_in_genre = []
        for record in reader:
        # why does print(record) not work?
            print(record)
            for single_genre in record['genre'].split(', '):
                if single_genre == genre:
                    songs_in_genre.append(record['song'])
        genre_song_dict[genre] = songs_in_genre

"""
The desired dictionary should look something like
{
'pop': [song1, song2, song3],
'rock': [song4, song1, song5],
'Dance/Electronic': [song6, song7, song8, song2]
}
"""

print(f"\nThis is the genre set:\n{genre_set}\n")
print(f"This is the final dictionary:\n{genre_song_dict}\n")
print(f"Done")


