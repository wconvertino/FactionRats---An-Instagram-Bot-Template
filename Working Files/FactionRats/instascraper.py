import instaloader
from instaloader import Instaloader, Profile
from itertools import dropwhile, takewhile
from datetime import datetime, date



def limitAmass(posts, limit, L):

    for post in posts:
            L.download_post(post, "posts")
            limit -= 1
            if limit <= 0:
                return()


def amassFromAllTime(num):

    

    profileList = open("profiles.txt", "r").read().split()
    L = instaloader.Instaloader()

    limit = num

    for profile in profileList:
        
        posts = instaloader.Profile.from_username(L.context, profile).get_posts()

        limitAmass(posts, limit, L)
        
            

def getImagesFromProfiles():

    profileList = open("profiles.txt", "r").read().split()
    L = instaloader.Instaloader()
    for profile in profileList:

        print(profile)

        posts = instaloader.Profile.from_username(L.context, profile).get_posts()

        dt = date.today()

        change = 0
        if dt.day < 2:
            change = 1
        
        SINCE = datetime(dt.year, dt.month, dt.day - change)
        UNTIL = datetime(dt.year, dt.month, dt.day)

        for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
            print(post.date)
            L.download_post(post, 'posts')

        print("Done with " + profile)



def getImagesFromHashtags():

    hashtagList = open("hashtags.txt", "r").read().split()

    L = instaloader.Instaloader()

    for tag in hashtagList:
        
        posts = L.get_hashtag_posts(tag)

        change = 0
        if dt.day < 2:
            change = 1
        
        SINCE = datetime(dt.year, dt.month, dt.day - change)
        UNTIL = datetime(dt.year, dt.month, dt.day)


        for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
            print(post.date)
            L.download_post(post, 'posts')
