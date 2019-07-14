import instapy
import instagramDriver as ID
import instascraper as scrape
import config
import os

#Allows you to store data in a text document







def cleanPosts():

    posts_dir = directory + r"\posts"
    
    test = os.listdir(posts_dir)

    for item in test:
        if item.endswith(".json") or item.endswith(".xz") or item.endswith(".txt") :
            os.remove(os.path.join(posts_dir, item))


def clearPostFolder():
    posts_dir = directory + r"\posts"
    
    test = os.listdir(posts_dir)

    for item in test:
        os.remove(os.path.join(posts_dir, item))

directory = config.getConfig("directory")

#Establishing UN and PW
username = config.getConfig("username")
password = config.getConfig("password")



#scrape.getImagesFromProfiles()
#scrape.getImagesFromHashtags()
scrape.amassFromAllTime(3)


cleanPosts()
ID.upload_posts(username,password)

clearPostFolder()
