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

    '''
    The loop below will go through one genre from the set first, in that genre, it will go through a single
    row in the csv, it will then go through the genre names, if the row's genre matches the current genre
    we are looping through, it will add that row's song name to a list, this list exists once per genre,
    this list is added to the dict, after all the rows are checked for one genre
    '''
    for genre in genre_set:
        songs_in_genre = []
        for record in reader:
        # why does print(record) not work?
            print(record)
            for single_genre in record['genre'].split(', '):
                if single_genre == genre:
                    songs_in_genre[single_genre].append(record['song'])
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