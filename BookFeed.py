#!/usr/bin/env python2.7

# 
import os

# calls CreateBookList for each subreddit
for subreddit in 1,2,3,4,5
    #returns list of books for each subreddit
    books = popen('./CreateBookList.py ' + '-s ' + subreddit )

    # makes html page for the values returned from CreateBookList
    links = popen('./GenerateHTML '  + books)
