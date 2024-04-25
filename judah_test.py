import sys
import argparse
import csv
import pandas as pd 

songs_csv = r'songs_normalize.csv'

with open(songs_csv, encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    all_songs_list = list(reader)

    genre_song_dict = {}
    genre_set = set()

    for one_row in all_songs_list:

        song_genre = one_row['genre']
    
        for single_genre in song_genre.split(', '):
            genre_set.add(single_genre)


    for genre in genre_set:
        songs_in_genre = []
        for one_row in all_songs_list:
            for single_genre in one_row['genre'].split(', '):
                if single_genre == genre:
                    songs_in_genre.append(one_row['song'])
        genre_song_dict[genre] = songs_in_genre

print(f"\nThis is the genre set:\n{genre_set}\n")
print(f"Done")


