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

def dataset_filtered():
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

    return genre_song_dict


"""input based on genre  -  Nathan """
def load_dataset(file_path):
    """Load dataset from CSV file
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
import pandas as pd

def recommend_songs_by_genre(dataset, genre):
    """
    Recommend songs based on the user's preferred genre.
    
    Args:
        dataset (pd.DataFrame): The dataset containing song information.
        genre (str): The user's preferred genre.
    
    Returns:
        A list of song recommendations (str) based on the genre.
    """
    
    genre_filtered = dataset[dataset['genre'].str.lower() == genre.lower()]
    
    
    if genre_filtered.empty:
        print("No songs found for the selected genre. Please try another genre.")
    else:
        print(f"Recommended songs in the {genre} genre:")
        for _, row in genre_filtered.iterrows():
            print(f"- {row['song_name']} by {row['artist']}")


if __name__ == "__main__":
    
    dataset_path = 'path/to/your/songs_dataset.csv'
    dataset = pd.read_csv(dataset_path)
    
    
    user_genre = input("Enter your preferred genre: ")
    recommend_songs_by_genre(dataset, user_genre)

'''
(Jason) user can then ask the program to list songs based on an inputted genre
allow user to filter songs by inputted year, output will change accordingly
'''

def add_to_dictionary():

    q1 = str(input("Would you like to filteer by year? yes/no")
    if q1 == "No" or "no":
                 exit()
    else:
        q2 = str(input("Does this song's genre exist in our table?")
                 
     if q2 == "No" or "no":
       user_genre = str(input("What genre would you like to add?")
        q4 = str(input("What song would you like to add? (Please note this song has to be within your selected genre.)")
                                                 
     if user_genre == "hip hop":
        queue.song(hip hop) # Adds a rap song to the queue
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

