'''
Lab 7
Name: Sjaakar * ALTIN * Campbell
Class: CIS41A PYTHON
Professor: The Awesome Mrs.Clare Nguyen
Week: 8
Date 05MAR2018
Description: this program shows the ranking of countries based on population growth.
'''


from untitled4.LABS.lab7.media import CD, DVD
from random import randint, seed

seed()
fileName = "lab7input.txt"


class MediaPlayer:
    def __init__(self):
        '''
        Media PLayer Constructor
        Creates a list of CDs and DVDs
        reads in the media from the file and promts user to enter any missing fields
        or skips improperly formatted data
        '''
        self._mediaList = []
        try:
            with open(fileName) as infile:
                for line in infile:
                    line = line.strip()
                    word = line.split(',')
                    if word[0] == "CD":
                        try:
                            myCD = CD(title=word[1].lstrip(" "), artist=word[2])
                        except IndexError:
                            cdTitle = input("Enter the title of the CD: ")
                            cdArtist = input("Enter the Artist: ")
                            myCD = CD(title=cdTitle, artist=cdArtist)
                        try:
                            myCD.setPlayTime(int(word[3]))
                        except IndexError:
                            print("Missing info on line:", line)
                            myCD.setPlayTime(int(input("Enter length of play time: ")))
                        try:
                            myCD.setTracks(int(word[4]))
                        except IndexError:
                            print("Missing info on line:", line)
                            myCD.setTracks(int(input("Enter number of tracks or 0 for no track info: ")))
                        self._mediaList.append(myCD)
                    elif word[0] == "DVD":
                        try:
                            myDVD = DVD(title=word[1].lstrip(" "))
                        except IndexError:
                            dvdTitle = input("Enter the title of the DVD: ")
                            myDVD = DVD(title=dvdTitle)
                        try:
                            myDVD.setRating(word[2].lstrip())
                        except IndexError:
                            print("Missing info on line:", line)
                            myDVD.setRating(input("Enter rating or None for no rating: "))
                        try:
                            myDVD.setPlayTime(int(word[3]))
                        except IndexError:
                            print("Missing info on line:", line)
                            myDVD.setPlayTime(int(input("Enter DVD play time: ")))
                        self._mediaList.append(myDVD)
                    else:
                        print("Error in line:", line)
                        print("### ignoring error")
        except FileNotFoundError as Error:
            print(fileName, "not found")
            print(str(Error))

    def play(self):
        '''
        Simulates playing the entire collection of media (CD and DVD's) by calling
        the play method of each song or DVD in the playlist
        :return: None
        '''
        print("Playing all of collection")
        for item in self._mediaList:
            print("Playing:", item)
            item.play()
            item.resetPlayed()
            print()

    def shuffle(self):
        '''
        Randomly selects a Media object from the list to play:
        - Simulates shuffle function of a media player
            continues to loop through the list of media until every CD/DVD's Played variable == true
            using the All function (which took me 3 days to figure out) And i still don't quite understand it.
        :return: None
        '''
        print()
        print("Playing on shuffle")
        numItems = len(self._mediaList)
        while not all((items.beenPlayed() for items in self._mediaList)):
            inque = randint(0, numItems-1)
            if not self._mediaList[inque].beenPlayed():
                self._mediaList[inque].play()
                print()
                print("Played:", self._mediaList[inque])



