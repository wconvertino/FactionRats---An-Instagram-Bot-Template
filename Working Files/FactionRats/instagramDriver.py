import os
import config
import random

def getDescription():

    descriptionList = open("captions.txt", "r").read().split("\n")

    i = random.randint(0,len(descriptionList))
    description = descriptionList[i]

    description += "  #meme #dank #dankmeme #tagyourself #memes #funny #tagyourselfmeme #modern #textpost #memesdaily #edgymemes #edgy #memepage #aesthetic #f4f #lfl #lb #comedy #textpost #gainpost #relatable #selfie #relatablepost #nichememe #tumblr #random #fashion #nichememes #tagyourfriends #hilarious"


    return(description)

def upload_posts(username, password):

    description = getDescription()

    directory = config.getConfig("directory") + "\posts"

    test = os.listdir(directory)


    for content in test:
        os.system("instapy -u " + username + " -p " + password + " -f \"" + directory + "\\" + content + "\" -t \"" + description + "\"")
    
