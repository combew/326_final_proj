import sys
import argparse
import csv
import pandas as pd 

'''
Judah
extract song name, and genre
Create a dictionary with genre as a key, songs as the values
'''
#def create_song_dictionary(file_path):

songs_csv = r'C:\Users\judah\OneDrive\Documents\GitHub\326_final_proj\songs_normalize.csv'

with open(songs_csv, encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    
    genre_song_dict = {}
    genre_set = set()

# some record has multiple genres, how can I add the song name of one entry as a value to 
# a separate dictionary with genres as a key

# this loop creates a set of genre names
    for record in reader:

        record_genre = record['genre']
    
        for single_genre in record_genre.split(', '):
            genre_set.add(single_genre)

# this loop will add the song name to genre_song_dict if its record's genre key has one in the set
    for record in reader:

        for single_genre in record_genre.split(', '):
            if single_genre in genre_set:
                print(f"{record['song']} is a {single_genre} song")



print(f"Done")