#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
This file is to edit the info of videos.
"""


import media
import fresh_tomatoes


The_Arrow = media.TV_show(
    "The Arrow", "A story of a DC super hero -- Oliver Queen",
    "Season 1",
    "http://img8.dm530.net/pic/uploadimg/2015-4/5092.jpg",
    "https://www.youtube.com/watch?v=ofzPONG8hDU")

Nikita = media.TV_show(
    "Nikita", "A girl named Nikita embarked on the raod to killer.",
    "Season 1",
    "http://stuffpoint.com/nikita/image/85100-nikita-nikita-poster.jpg",
    "https://www.youtube.com/watch?v=IhelGgaa2Wg")

Scorpion = media.TV_show(
    "Scorpion", "The high IQ team helps DHS with defending attack.",
    "Season 1",
    "https://s-media-cache-ak0.pinimg.com/originals/96/23/32/96233256645e445e7ab6c2775d80cba5.jpg",  # NOQA
    "https://www.youtube.com/watch?v=l4QFpheS_JQ")

Sky_High = media.Movie(
    "Sky High", "A story about Superman's son",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Sky_High_movie_poster.jpg",
    "https://www.youtube.com/watch?v=G7aMWVN1ThM")

El_bar = media.Movie(
    "El bar", "Who went our, who got killed",
    "http://cinehorizontes.com/wp-content/uploads/el-bar-alex-de-la-iglesia-508x320.jpg",  # NOQA
    "https://www.youtube.com/watch?v=PTazqyeYg3Y")

She_is_the_Man = media.Movie(
    "She is the man", "Who says a girl cannot play football better than boys?",
    "https://www.jbhifi.com.au/FileLibrary/ProductResources/Images/176148-L-LO.jpg",  # NOQA
    "https://www.youtube.com/watch?v=D4OhwrMidSU")

# Put the videos in a variable
videos = [
    The_Arrow,
    Nikita,
    Scorpion,
    Sky_High,
    El_bar,
    She_is_the_Man
    ]
# Call the function to run the program
fresh_tomatoes.open_movies_page(videos)
