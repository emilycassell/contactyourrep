import praw
#__init__(reddit, id=None, url=None, _data=None)
reddit = praw.Reddit(client_id='CLIENT_ID',
                     client_secret="CLIENT_SECRET", password='PASSWORD',
                     user_agent='USERAGENT', username='USERNAME')

r = praw.Reddit('Comment Scraper 1.0 by u/_Daimon_ see '
                'https://praw.readthedocs.io/en/latest/'
                'pages/comment_parsing.html')
r.login('contactyourrep', 'treehacks2018')
submission = r.get_submission(submission_id='11v36o')
flat_comments = praw.helpers.flatten_tree(submission.comments)
already_done = set()

subreddit = r.get_subreddit('test')
subreddit_comments = subreddit.get_comments()
for comment in subreddit_comments:
    if comment.body == "Ocasio" and comment.id not in already_done:
        comment.reply('Contact your representative today!')
        already_done.add(comment.id) 





print ("working")