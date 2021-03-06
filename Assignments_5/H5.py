import json
import MusicDB


MusicDB.clearFile ()
MusicDB.callMenu ()

while True:
    command = input("Enter one of the listed commands: ")
    if command == "add":
        MusicDB.addSong ()
    elif command == "save" and MusicDB.totalSongs <= 8:
        MusicDB.saveSong ()
        MusicDB.totalSongs = MusicDB.totalSongs + 1
    elif command == "save" and MusicDB.totalSongs > 8:
        print("Too many songs.")
    elif command == "clear":
        MusicDB.clearFile ()
        totalSongs = 0
        print("Database cleared.")
    elif command == "list":
        MusicDB.listSong ()
    elif command == "help":
        MusicDB.callMenu ()
    elif command == "exit":
        break
    else:
        print("Error, that's not a valid command")
        continue