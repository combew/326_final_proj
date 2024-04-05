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

