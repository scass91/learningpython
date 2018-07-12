#July 12th 2018
#start with albums.py, write a while loop which allows users to enter an album
#title & artist, once the information is received, call make_album() with the
#users input and print the created dictionary

def make_album(artist_name, album_title, tracks=""):
    """Returns information about musical albums"""
    album = {"Artist" : artist_name, "Title" : album_title}
    if tracks:
        album["Tracks"] = tracks
    return album

while True:
    print("\nPlease tell me your favourite music album & artist: ")
    print("(Enter 'q' to quit at any time)")

    title = input("Album name: ")
    if title == 'q':
        break

    artist = input("Artist name: ")
    if artist == 'q':
        break

    album = make_album(artist, title)
    print(album)
