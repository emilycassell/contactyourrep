import praw
import config
import time
import os
import requests

main_api = 'https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators?'
address = 'San Francisco'
level = NATIONAL_LOWER
url = main_api + urllib.parse.urlencode({'address': address}{'level': level})

api = requests.get('https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators?address=San Francisco&level=NATIONAL_LOWER')



print(api.status_code)

def bot_login():
    print('Logging Into Reddit...')
    r = praw.Reddit(user_agent="contact your rep bot", 
                client_id=config.client_id, 
                client_secret=config.client_secret,
                username=config.username, 
                password=config.password)
    print('Logged in')
    return r

def run_bot(r, repliedto):
    for comment in r.subreddit('test').comments(limit=25):
    
        if "test" in comment.body and comment.id not in repliedto and comment.author != r.user.me():


            print("String found !")
            #comment.reply("Hey there, this is a test for the coolest bot ever.")
            print("replied to comment" + comment.id)
            repliedto.append(comment.id)

            with open ("repliedto.txt", "a") as f:
                f.write(comment.id + "\n")

    print("sleeping for ten seconds...")
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("repliedto.txt"):
        repliedto = []
    else:
        with open("repliedto.txt", "r") as f:
            repliedto = f.read()
            repliedto = repliedto.split("\n")
            repliedto = filter(None, repliedto)
            repliedto=list(repliedto)
    return repliedto
repliedto = []
repliedto=get_saved_comments()

print(repliedto)

while True:
    r = bot_login()
    run_bot(r, repliedto)