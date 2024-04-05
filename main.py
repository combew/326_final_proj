"""A template for a python script deliverable for INST326.

Drivers: Jason De Azevedo, Nathan Bogin, Judah Kamadinata, Omar
Assignment: Final Project
Date: 4_1_24

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import sys
import argparse
import csv

'''
Judah
extract song name, and genre
'''
#def create_song_dictionary(file_path):

csv_rows = []
file_path = "songs_normalize.csv"
with open(file_path, 'r') as fc:
    csv_text = fc.read()
    # csv_obj is an object as a result of the csv.reader(fc) function
    print(csv_text)

'''
Nathan
Allow user to input genre likes
'''

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

