import praw
import json
from praw.models import MoreComments, comment_forest
def get_credentials():
    f = open("credentials", "r")
    return f.read().split('\n')

def get_reddit():
    g=get_credentials()
    return praw.Reddit(user_agent=g[0], client_id=g[1], client_secret=g[2], username=g[3], password=g[4])

def get_comments(sub):
    reddit = get_reddit()
    subreddit = reddit.subreddit(sub).hot()
    comments = []
    for post in subreddit:
        thread = reddit.submission(id=post)
        for comment in thread.comments:
            if isinstance(comment, MoreComments):
                continue
            comments.append(comment.body)
    return comments


def write_to_file(w):
    print (w)
    write = json.dumps(w)
    f = open('data', 'w')
    f.write(write)

c = get_comments('barnard')
write_to_file(c)
