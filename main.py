"""A template for a python script deliverable for INST326.

Drivers: Jason De Azevedo, Nathan Bogin, Judah Kamadinata, Omar
Assignment: Final Project
Date: 4_1_24

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

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

 
df = pd.read_csv("songs_normalize.csv")

print(df.head())


"""input based on genre  -  Nathan """
def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    return dataset

def filter_genre(dataset, genre):
    filtered_dataset = dataset[dataset['genre'] == genre]
    return filtered_dataset

def main():
    dataset = 'data/songs_dataset.csv'
    songs = load_dataset(dataset)
    
    user_genre = input("Enter your preferred genre: ")
    filtered_songs = filter_genre(songs, user_genre)
    
    print(filtered_songs)

if __name__ == "__main__":
    main()

'''
(Omar Humeida) match user genre tastes with existing songs and their genre
output a list of songs that fit their genres 
'''

'''
(Jason) user can then ask the program to list songs based on an inputted genre
allow user to filter songs by inputted year, output will change accordingly 
(Jason) user can also choose to change the genre/year again
'''

'''
(judah) user can add song/genre
'''

