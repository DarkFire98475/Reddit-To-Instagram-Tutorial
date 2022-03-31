from RedDownloader import RedDownloader
from instagrapi import Client

import time
import os
import random

# downloading posts from reddit
def GetMeme():
    post = RedDownloader.DownloadBySubreddit('memes' , 1 , output='meme' , SortBy='new')
    author = post.GetPostAuthors()[0]
    return author

# sign in to instagram
client = Client()
client.login('dark_fire9847' , 'devaragam9847')

# prepare the post for uploading
def GenerateCaption():
    captions =[
        '#dankmeme #memes #dankmemes #meme #dank #memesdaily #funnymemes #funny #edgymemes #lol #offensivememes #dailymemes #lmao #memepage #funnymeme #humor #comedy #memestagram #follow #anime #like #memer #tiktok #dankmemesdaily #fun #instagram #ol #love #fortnite #bhfyp',
        '#shitpost #bhfyp #instagood #cringe #spicymemes #memez #funnyvideos #memelord #offensive #haha #explorepage #shitposting #minecraft #edgymeme #dankmemez #darkmemes #hilarious #darkhumor #animememes #memeaccount #offensivememe #lmfao #memegod #explore #dankvideos #deepfriedmemes #memesespa #tiktokmemes #bestmemes #jokes',
        '#dankmeme #meme #explorepage #bhfyp #tiktok #dankmemes #funnymemes #memesdaily #humor #comedy #dank #lmao #fortnite #haha #edgymemes #offensivememes #dankmeme #edgy #funnyvideos #jokes #hilarious'
    ]
    return random.choice(captions)

def CleanUp():
    try:
        os.remove('meme/meme1.jpeg')
    except:
        pass

# upload the post
while True:
    author = GetMeme()
    hashtags = GenerateCaption()
    caption = f'Credits to {author} \n {hashtags}'
    try:
        client.photo_upload('meme/meme1.jpeg' , caption)
    except Exception as e:
        print(e)
    finally:
        print('Posted')
    time.sleep(15*60)
    print('Sleeping...')
    CleanUp()
