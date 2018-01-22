#!/usr/bin/env python
# -*- coding: utf-8 -*


import webbrowser

"""
This file is to create classes which have variables that most videos contain..
"""


class Video():
    def __init__(self, title, storyline):
        self.title = title
        self.storyline = storyline


# Inherit variables from class Video
class Movie(Video):
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


# Inherit variables from class Video
class TV_show(Video):
    def __init__(self, title, storyline, season, poster_image, trailer_youtube):
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
    webbrowser.open(self.trailer_youtube_url)
