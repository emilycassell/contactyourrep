import praw
import time
import random

def run():
    print('Logging Into Reddit...')
    #Create Bot with login and private key - username - password
    bot = praw.Reddit(user_agent='Example Bot 1', client_id='', client_secret='',
        username='contactyourrep', password='treehacks2018')
    print('Logged in')

    subreddit = bot.subreddit('test')                          #Enter Subreddit
    for submission in subreddit.stream.submissions():
        print(submission.title)
        author = str(submission.author)
        reply_text = 'hello! u/' + author + ' Welcome to the XYZ sub!  \n \n ' 
        #print(reply_text)
        submission.reply(reply_text)
        time.sleep(3)

if __name__ == '__main__':
    run()