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

genre_input = input(f"Print songs based off one genre from: {genre_set}\n")
print(f"Here are {genre_input} songs!\n{genre_song_dict[genre_input]}")

song_input = input(f"We can find songs based off another song too! Just enter the name here:\n")
thing = [genre for genre, song in genre_song_dict.items() if song_input == song]
print(thing)