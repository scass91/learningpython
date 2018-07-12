#July 12th 2018
#write a function called make_album(), that builds a dictionary describing
#a music album. The function should take an artist name and an album title,
#returning a dictionary containing these 2 pieces of information. Use the
#function to make three dictionaries, print each return value to show the info
#has been correctly stored

def make_album(artist_name, album_title, tracks=""):
    """Returns information about musical albums"""
    album = {"Artist" : artist_name, "Title" : album_title}
    if tracks:
        album["Tracks"] = tracks
    return album

album = make_album("Eminem", "The Eminem show")
print(album)
album = make_album("Kanye West", "ye", tracks = 7)
print(album)
album = make_album("Alexisonfire", "Watch out!")
print(album)
