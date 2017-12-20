import praw
from praw.models import MoreComments, comment_forest
def get_credentials():
    f = open("credentials", "r")
    return f.read().split('\n')
g=get_credentials()
print(g)
reddit = praw.Reddit(user_agent=g[0],
                     client_id=g[1], client_secret=g[2],
                     username=g[3], password=g[4])

subreddit = reddit.subreddit(display_name='funny')

questions = ['what is', 'who is', 'what are']
#something = reddit.multireddit('TheOnion', 'nottheonion').hot()
something = reddit.subreddit('politics').hot()

print (something)
ret = ""
for thing in something:
    thread = reddit.submission(id=thing)
    #ret+= thing.title + '\n'
    for top in thread.comments:
        if isinstance(top, MoreComments):
            continue
        ret+=(top.body) + "\n"
f = open('data2', 'w')
f.write(ret)
'''for submission in subreddit.stream.submissions():
    normalized_title = submission.title.lower()
    url = submission.url
    print (type(submission))
    for question_phrase in questions:
        if question_phrase in normalized_title:
        # do something with a matched submission
            print ([normalized_title, url])
            break'''
#print (c)
#for thing in c:
#    print (thing)
#for top_level_comment in submission.comments:
#    if isinstance(top_level_comment, MoreComments):
#        continue
#    print(top_level_comment.body)

#r=reddit#praw.Reddit('demo')
#subreddit=r.subreddit('stackoverflow')

#for submission in subreddit.get_hot(limit=10):
#    print (submission.title)
