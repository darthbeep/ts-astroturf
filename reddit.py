import praw
import json
from praw.models import MoreComments, comment_forest
def get_credentials():
    f = open("credentials", "r")
    return f.read().split('\n')

def get_reddit():
    g=get_credentials()
    return praw.Reddit(user_agent=g[0], client_id=g[1], client_secret=g[2], username=g[3], password=g[4])

def get_subreddits():
    f = open('subreddit_list', 'r')
    return f.read().split()

def get_comments(sub):
    reddit = get_reddit()
    subreddit = reddit.subreddit(sub).hot(limit=10)
    comments = []
    for post in subreddit:
        #i=0
        thread = reddit.submission(id=post)
        for comment in thread.comments:
            if isinstance(comment, MoreComments):
                continue
            comments.append(comment.body)
            #i+=1
            #if i > 2:
            #    break
    return comments

def get_all_comments():
    inputs = get_subreddits()
    subreddit_comments = {}
    for inp in inputs:
        print (inp)
        subreddit_comments[inp] = get_comments(inp)
        f = open(inp, 'w')
        f.write(json.dumps(subreddit_comments[inp]))
    return subreddit_comments


def write_to_file(w):
    write = json.dumps(w)
    f = open('data.json', 'w')
    f.write(write)

write_to_file(get_all_comments())
