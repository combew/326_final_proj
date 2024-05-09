"""Python script deliverable for INST326.

Drivers: Jason De Azevedo, Nathan Bogin, Judah Kamadinata, Omar Humeida
Assignment: Final Project
"""

import sys
import argparse
import csv
import pandas as pd 
import unittest 
from unittest.mock import patch

def dataset_filtered():
    '''
    This function opens the csv of songs and creates a dictionary for later use

    Args:
    - none

    Returns:
    - genre_song_dict (dictionary): A dictionary with a genre as a key, and a list of all the songs in that
        genre as the value
    '''
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

    return genre_song_dict, genre_set

def prompt_user_for_genre(genre_song_dict):
    '''
    Prompts user for a genre to pick songs from

    Args:
    - genre_song_dict (dict): a dictionary of songs sorted by genre

    Return:
    - genre_input (str): a user inputted str
    '''
    print(f"Available genres: {', '.join(sorted(genre_song_dict.keys()))}")
    genre_input = input("Enter a genre to print songs from: ")
    return genre_input

def print_songs_for_genre(genre_song_dict, genre_input):
    '''
    Prints songs from a genre

    Args:
    - genre_song_dict (dict): a dictionary of songs sorted by genre
    - genre_input (str): a user inputted str

    Return:
    - none
    '''
    if genre_input in genre_song_dict:
        print(f"Here are {genre_input} songs!\n{genre_song_dict[genre_input]}")
    else:
        print("Genre not found. Please try again with a valid genre from the list.")

def print_songs_from_user_inputted_song(song_name, genre_song_dict):
    """
    Print songs that are in the same genre as the song inputted by the user.
    
    Args:
        song_name (str): The song name inputted by the user.
        genre_song_dict (dict): Dictionary mapping genres to lists of songs.
    
    Returns:
        None: Prints a list of song recommendations from the same genre or an error message.
    """
    song_genre = None
    for genre, songs in genre_song_dict.items():
        if song_name in songs:
            song_genre = genre
            break

    if song_genre:
        print(f"Songs in the same genre as '{song_name}' ({song_genre} genre):")
        for song in genre_song_dict[song_genre]:
            if song != song_name:  
                print(f"- {song}")
    else:
        print("Song not recognized. Please try another song.")

def add_to_dictionary(genre_song_dict):
    '''
    Allows users to add elements to our dictionary

    Args:
    - genre_song_dict (dict): a dictionary of songs sorted by genre

    Returns:
    - 0 (int): only in certain circumstances
    '''
    song_add = input("Would you like to add a song? yes/no\n").lower()
    if song_add == "no":
        print("The function will now exit.")
        return 0
        
    elif song_add == "yes":
        song_name = str(input("Enter the name of the song:\n"))
        genre = input("Enter the genre of the song:\n")
        
        if genre not in genre_song_dict.keys():
            print(f"'{genre}' does not exist in the dictionary.")
            new_genre = input("Enter the genre you would like to add (case sensitive):\n")
            genre_song_dict[new_genre] = [song_name]
            print(f"'{song_name}' added to '{new_genre}'.")
            
        else:
            print(f"The genre '{genre}' exists.")
            add_to_existing_genre = input(f"Do you want to add '{song_name}' to '{genre}'? (yes/no):\n").lower()
            if add_to_existing_genre == 'yes':
                genre_song_dict[genre].append(song_name)
                print(f"Song '{song_name}' added to genre '{genre}'.")
            else:
                print("Okay, not adding the song.")
    
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    '''
    Calls a specific function based off user inputs, only stops looping when the user decides to quit

    Args:
    - None

    Returns:
    - none, only prints
    '''
    d, genre_set = dataset_filtered()
    print(d)
    while True:

        user_input = input('\nWould you like to search for songs based off genre, based off a song, add to our list of songs, see our song list, or quit the program? (genre/song/add/list/quit)\n')

        if user_input == 'genre':
            genre_input = prompt_user_for_genre(d)
            print_songs_for_genre(d, genre_input)
        
        elif user_input == 'song':
            user_song = input('What song would you like to find similar songs for?\n')
            print_songs_from_user_inputted_song(user_song, d)
            
        elif user_input == 'add':
            add_to_dictionary(d)

        elif user_input == "list":
            print(d)

        elif user_input == 'quit':
            print("Thank you for using our program :D")
            quit()

        else:
            'please input a valid option'

if __name__ == "__main__":
    class TestFunctions(unittest.TestCase):

        def setUp(self):
            self.genre_song_dict = {
                'Rock': ['Song1', 'Song2', 'Song3'],
                'Pop': ['Song4', 'Song5']
            }

        @patch('builtins.input', return_value='Rock')
        def test_prompt_user_for_genre(self, mocked_input):
            genre_input = prompt_user_for_genre(self.genre_song_dict)
            self.assertEqual(genre_input, 'Rock')

        @patch('builtins.print')
        def test_print_songs_for_genre_valid(self, mocked_print):
            print_songs_for_genre(self.genre_song_dict, 'Rock')
            mocked_print.assert_called_with("Here are Rock songs!\n['Song1', 'Song2', 'Song3']")

        @patch('builtins.print')
        def test_print_songs_for_genre_invalid(self, mocked_print):
            print_songs_for_genre(self.genre_song_dict, 'Unknown')
            mocked_print.assert_called_with("Genre not found. Please try again with a valid genre from the list.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        unittest.main(argv=[''], exit=False)
    else:
        main()
