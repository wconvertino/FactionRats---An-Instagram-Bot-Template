# FactionRats
A configurable template for an Instagram bot that automatically posts pictures/videos from other accounts.

Example account - "FactionRats":
https://www.instagram.com/factionrats/

# How to use
To set it up, all you need to do is go into the config.txt file, and write the username/password of the instagram account you would like to use, and the directory for the FactionRats folder. Then, to launch, run main.py.

To change the hashtags provided, accounts scraped, or captions given, simply edit the text files. Each line should contain a different entry.

Every entry in the "hashtags" file, as well as a randomly selected entry from the captions file, will be added to each new post.

# Dependencies
Instapy-cli,
Instaloader, and
the built-in OS, datetime, random, and itertools modules
