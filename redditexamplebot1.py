import praw
import config
import time
import os
import requests
import urllib.parse
from keywords import keyworddict
from textblob import TextBlob

from parsinjson import create_response 
from parsinjson import ngrams
from parsinjson import combine_ngrams
#from . import winrandom


main_api = 'https://q4ktfaysw3.execute-api.us-east-1.amazonaws.com/treehacks/legislators?'
level = 'NATIONAL_LOWER'
headers = { 'X-API-KEY': '2e1uvo7yeX50ZGHvctPxi8ZWubhggyOydIWvOa5c'}



def bot_login():
    print('Logging Into Reddit...')
    r = praw.Reddit(user_agent="contact your rep bot", 
                client_id=config.client_id, 
                client_secret=config.client_secret,
                username=config.username, 
                password=config.password)
    print('Logged in')
    return r

r = bot_login()

def run_bot(r, repliedto):
    for comment in r.subreddit('contactyourrep').comments(limit=25):
    
        #if "San Francisco" in comment.body and comment.id not in repliedto and comment.author != r.user.me():

        #print(comment)
        cbody=comment.body
        cbody=ngrams(cbody, 2)
        cbody=combine_ngrams(cbody)



        #print(cbody)
        for word in cbody:
            #print(word)

            if word in keyworddict:
                print(word)
            
                #if comment.id not in repliedto and comment.author !=r.user.me():
                if comment.author !=r.user.me():
                    with open ("repliedto.txt", "a") as f:
                            f.write(comment.id + "\n")
                    text =str(comment.body)
                    #print(type(comment))
                    analysis = TextBlob(text)
                    print(analysis.sentiment[0])
                    if analysis.sentiment[0]<.4:
                        address = keyworddict[word]
                        print(address)
                        url = main_api + urllib.parse.urlencode({'address': address})+urllib.parse.urlencode({'level': level})
                        json_data = requests.get(url, headers=headers).json()
                        #print(json_data)
                        contactdict = create_response(json_data)
                        #print(contactdict)
                        #print(contactdict)


                        replytext = ("Mad about what’s going on in your neighborhood? Don’t just complain on reddit, do something! Contact your representatives today! \n\n" + " ".join(str(x) for x in contactdict) + "Find scripts for issues you care about [Here](https://5calls.org/) \n\n" + "If you don’t actively participate in our democracy, Russian bots like me will win. \n\n **Brought to you by treehacks and Phone2action (phone2action.com).")
                        #replytext = ("Mad about what’s going on in your neighborhood? Don’t just complain on reddit, do something! Contact your representative today!" + " ".join(str(x) for x in contactdict) + "Find scripts for issues you care about [Here](https://5calls.org/)" + "If you don’t actively participate in our democracy, Russian bots like me will win.  **Brought to you by treehacks and Phone2action (phone2action.com).")
                   
                        print(replytext)

                    
                        comment.reply(replytext)
                        print("replied to comment" + comment.id)
                        #repliedto.append(comment.id)

                        

            print("sleeping for a sec...")
            time.sleep(5)


#bot_login()
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
    run_bot(r, repliedto)
