'''

def dataset_filtered(path):

    this is judah's function, the function will take in the path to songs and create and return a dictionary 
    (if i stick with using the csv module method) OR a table (if i take jaden's suggestion of using pandas) 
    that has songs filtered by their genre

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

def main() Judah will work on this after you guys have finished ur functions:

    d = dataset_filtered('songs_normalize.csv')

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

if __
    main()
'''