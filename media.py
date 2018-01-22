#!/usr/bin/env python
# -*- coding: utf-8 -*


import webbrowser


class Video():
    # to create classes which have variables that most videos contain
    def __init__(self, title, storyline):
        """
        Initialize class Video() when called
        And store info to the variables
        """
        self.title = title
        self.storyline = storyline


class Movie(Video):
    """
    Inherit variables from class Video
    Append some movie elements
    """
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        """
        Initialize class Movie() when called
        And store info to the variables
        """
        Video.__init__(self, title, storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


class TV_show(Video):
    """
    Inherit variables from class Video
    Append some TV show elements
    """
    def __init__(
                self, title, storyline, season, poster_image, trailer_youtube):
        """
        Initialize class TV_show() when called
        And store info to the variables
        """
        Video.__init__(self, title, storyline)
        self.season = season
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
"""
To use these classes, use following format:

Movie = ("title", "storyline", "poster_image", "trailer_youtube")
TV_show = ("title", "storyline", "season", "poster_image", "trailer_youtube")

"""


def show_trailer(self):
    # when called, run the project
    webbrowser.open(self.trailer_youtube_url)
