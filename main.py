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
    """Load dataset from a CSV file
    Args:
        file_path (str): The path to the CSV file
    Returns:
        The loaded dataset
    """
    dataset = pd.read_csv(file_path)
    return dataset

def filter_genre(dataset, genre):
    """Filter dataset based on genre
    Args:
        dataset: The dataset containing song information
        genre: The genre to filter the dataset by
    Returns:
        The filtered dataset containing songs of the specified genre by user
    """
    filtered_dataset = dataset[dataset['genre'] == genre]
    return filtered_dataset

def main():
    """Main function to run the program."""
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
'''
if user_genre == "hip hop":
 queue.song(hip_hop) # Adds a rap song to the queue
elif user_genre == "pop":
 queue.song(pop) # Adds a pop song to the queue
elif user_genre == "country":
 queue.song(country) # Adds a country song to the queue
elif user_genre == "rock":
 queue.song(rock) # Adds a rock song to the queue
elif user_genre == "blues":
 queue.song(blues) # Adds a blues song to the queue
 
'''
(Jason) user can also choose to change the genre/year again
'''

'''
(judah) user can add song/genre
'''

