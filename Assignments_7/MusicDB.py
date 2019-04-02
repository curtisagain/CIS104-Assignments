import json
totalSongs = 0

Song = {
    "Title": None,
    "Artist": None,
    "Album": None,
    "Track": None,
    "Year": None,
    "Genre": None}

def addSong(): # char limits from https://stackoverflow.com/questions/28465779/how-do-i-limit-the-amount-of-letters-in-a-string
    while True:
         Song["Title"] = input("Enter song tile: ") 
         if len(Song["Title"]) <= 64:
             break
         else:
             print("That title is too long")
    while True:
        Song["Artist"] = input("Enter artist name: ")
        if len(Song["Artist"]) <= 32:
            break
        else:
             print("That artist name is too long")
    while True:
         Song["Album"] = input("Enter album title: ")
         if len(Song["Album"]) <= 64:
             break
         else:
             print("That album title is too long")
    Song["Track"] = input("Enter track number: ")
    Song["Year"] = input("Enter year: ")
    Song["Genre"] = input("Enter genre: ")

def saveSong():
    if Song["Title"] != None:
        writefile = open("MusicDB.txt", "a")
        writefile.write(json.dumps(Song))
    elif Song["Title"] == None:
        print("No songs to save. ")

def clearFile(): #clears the json file
    file = open("MusicDB.txt", "w")
    file.truncate(0)


    f = open("MusicDB.txt", "r")
    for entry in f:
        entry = []
        emptyEntry = entry.replace('"', '').strip("{").strip("}").strip(",").split("}{")
        list(dict.values(f)) = emptyEntry 
def listSong(): 
    if totalSongs == 0:
        print("No songs on list, try saving. ")
    else:
        count = 0
        f = open("MusicDB.txt", "r")
        for entry in f:
            empty = []
            emptyEntry = entry.replace('"', '').strip("{").strip("}").strip(",").split("}{") #prints the songs without the formatting from json
        for s in emptyEntry:
            count = count + 1
            print("Song #" ,count, ":" ,s, "\n")

def callMenu():
    print("add : Add a new song to the music database\n"
     "list : List the songs in the music database\n"
     "save : Save the music database\n"
     "help : Display this menu\n"
     "clear : Clear the music database\n"
     "exit : Exit the Program\n")