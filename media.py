'''
Lab 7
Name: Sjaakar * ALTIN * Campbell
Class: CIS41A PYTHON
Professor: The Awesome Mrs.Clare Nguyen
Week: 8
Date 02MAR2018
Description: this program shows the ranking of countries based on population growth.
'''

import time
time.sleep(0.5)


class Media:
    def __init__(self, title, playTime=0, played=False):
        '''
        Constructor for the Media (parent) Class
        :param title: required variable used to initialize title instance var (title of media)
        :param playTime: optional variable used to initialize playtime instance var (length of media in seconds?)
        :param played: optional variable used to initialize boolean played instance var (has the song been played)
        '''
        self._title = title
        if isinstance(playTime, int):
            self._playTime = playTime
        else:
            # !!!!!!!!!!!!!!!
            self._playTime = 0
        self._played = played

    def __repr__(self):
        '''
        :return: a string representing the title of the object
        '''
        return self._title

    def setPlayTime(self, playtime):
        '''
        set's the playtime
        :param playtime: length of media play time in seconds
        :return: None
        '''
        if isinstance(playtime, int):
            self._playTime = playtime

    def play(self):
        '''
        Simulates a media being played
        :return: None
        '''
        self._played = True
        for count in range(1, self._playTime+1):
            print(count, end=' ', flush=True)
            time.sleep(0.5)

    def setTitle(self, title):
        '''
        Sets the title of the media
        :param title: Title of media
        :return: None
        '''
        self._title = title

    def getTitle(self):
        '''
        :return: the title of the media
        '''
        return self._title

    def getPlayTime(self):
        '''
        :return: the Playtime
        '''
        return self._playTime

    def beenPlayed(self):
        '''
        :return: boolean of weither an item has been played
        '''
        return self._played

    def setPlayed(self):
        '''
        sets the boolean var to True
        :return: None
        '''
        self._played = True

    def resetPlayed(self):
        '''
        sets played back to False
        :return: None
        '''
        self._played = False


class CD(Media):
    def __init__(self, title, artist, playTime=0, tracks=0, played=False):
        '''
        CD constructor
        :param title: inherited
        :param artist: Artist of the song
        :param playTime: inherited
        :param tracks: number of track on CD
        :param played: inherited
        '''
        super(CD, self).__init__(title, playTime, played)
        self._artist = artist
        if isinstance(tracks, int):
            self._tracks = tracks
        else:
            self._tracks = 0

    def setTracks(self, tracks):
        '''
        sets the tracks
        :param tracks: number of track on CD
        :return: NOne
        '''
        if isinstance(tracks, int):
            self._tracks = tracks
        else:
            self._tracks = 0

    def setArtist(self, artist):
        '''
        Sets The Artist var
        :param artist: Artist or group who took credit for the song (who actually writes their own music anymore)
        :return: None
        '''
        self._artist = artist

    def getTracks(self):
        '''
        :return: returns the amount of tracks
        '''
        return self._tracks

    def __repr__(self):
        '''
        :return: a string representing the object
        '''
        CDdata = self._title + " by" + self._artist + ", " + str(self._tracks) + " tracks, play time: " \
                 + str(self.getPlayTime())
        return CDdata


class DVD(Media):
    def __init__(self, title, playTime=0, played=False, rating=None):
        '''
        DVD Constructor
        :param title: inherited
        :param playTime: inherited
        :param played: inherited
        :param rating: Movie Rating
        '''
        super(DVD, self).__init__(title, playTime, played)
        if rating is not None and not str.isdigit(rating):
            self._rating = rating

    def setRating(self, rating):
        '''
        sets the rating
        :param rating: Rating of the movie
        :return: None
        '''
        if rating == "None" or rating == "none":
            self._rating = "No Rating"
        elif not str.isdigit(rating):
            self._rating = rating

    def getRating(self):
        '''
        :return: the rating of the movie
        '''
        return self._rating

    def __repr__(self): ##SUPER?
        '''
        :return: a string representing the object
        '''
        DVDdata = self._title + ", Rating: " + self._rating + ", play time: " + str(self.getPlayTime())
        return DVDdata


