"""A template for a python script deliverable for INST326.

Drivers: Jason De Azevedo, Nathan Bogin, Judah Kamadinata, Omar Humeida
Assignment: Final Project
Date: 4_1_24

"""

import sys
import argparse
import csv
import pandas as pd 

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

    return genre_song_dict

# this is the new structure of our code, you don't need to keep the function names cuz ik they're very long LMAO
'''
def print_songs_from_user_inputted_genre(genre, dictionary/table):

    this is nathan's function, this function will take in a genre typed in by the user, this function will
    find which songs match the genre and print it
    if the user types a genre we don't have in our dictionary/table, it should print some error and tell the
    user we don't recognize that genre

def print_songs_from_user_inputted_song(song name, dictionary/table):

    this is omar's function, this function will take in a song typed in by the user, and print songs that are
    in the same genre
    if the user types a song we don't have in our dictionary/table, it should print some error and tell the
    user we don't recognize that song

def add_to_dictionary(no parameters):

    this is jason's function, this function will ask if the user wants to add a song, if they say no, the 
    function ends. If they say yes, then we ask them if that song's genre exists in our dictionary/table.
    If the genre doesn't exist, ask them what genre they would like to add, AND the song they would like to
    add (this song would have to be in the new genre they want to add). If the genre DOES exist, ask them
    to type which genre they would like to add to (case sensitive), and the song they would like to add to
    that genre.

def main():

    d = dataset_filtered()

    while True: < basically this while loop will run forever until the user inputs 'quit'

        print(the filtered dataset) #so the user can see what genres and song exist

        input = 'would you like to search for songs based off genre, based off a song, add to our 
        list of songs, or quit the program?'

        if input == genre:
            genre = 'what genre would you like to search for?'
            print_songs_from_user_inputted_genre(genre, the filtered dataset)
        
        elif input == song:
            song = 'what song would you like to find similar songs for?'
            print_songs_from_user_inputted_song(song name, dictionary/table)

        elif input == add:
            add_to_dictionary(no parameters)

        elif input == quit:
            quit()

        else:
            'please input a valid option'

if __name__ == "__main__":
    main()
'''

'''
(Omar Humeida) match user genre tastes with existing songs and their genre
output a list of songs that fit their genres 
'''
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
'''
(Jason) user can then ask the program to list songs based on an inputted genre
allow user to filter songs by inputted year, output will change accordingly
'''

def add_to_dictionary(songs_normalize):

    
    song_add = input("Would you like to add a song? yes/no").lower()
    if song_add == "no":
        print("The function will now exit.")
                return 0
        
    elif song_add == "yes":
        song_name = str(input("Enter the name of the song: "))
        genre = input("Enter the genre of the song: ")
        
        if genre not in songs_normalize:
            print(f"'{genre}' does not exist in the dictionary.")
            new_genre = input("Enter the genre you would like to add (case sensitive): ")
            songs_normalize[new_genre] = [song_name]
            print(f"'{song_name}' added to '{new_genre}'.")
            
        else:
            print(f"The genre '{genre}' exists.")
            add_to_existing_genre = input(f"Do you want to add '{song_name}' to '{genre}'? (yes/no): ").lower()
            if add_to_existing_genre == 'yes':
                song_normalize[genre].append(song_name)
                print(f"Song '{song_name}' added to genre '{genre}'.")
            else:
                print("Okay, not adding the song.")
    
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        add_to_dictionary(songs_normalize)


def main(): #Judah's function

    d = dataset_filtered()

    while True:

        print(d)

        user_input = input('Would you like to search for songs based off genre, based off a song, add to our list of songs, or quit the program? (genre/song/add/quit)\n')

        if user_input == 'genre':
            user_genre = 'what genre would you like to search for?'
            print_songs_from_user_inputted_genre(user_genre, d)
        
        elif user_input == 'song':
            user_song = 'what song would you like to find similar songs for?'
            print_songs_from_user_inputted_song(user_song, d)

        elif user_input == 'add':
            add_to_dictionary()

        elif user_input == 'quit':
            print("Thank you for using our program :D")
            quit()

        else:
            'please input a valid option'

if __name__ == "__main__":
    main()