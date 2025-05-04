import os
from authenticate import authenticate_reddit
import pandas as pd

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Project Root: {project_root}")

reddit_instance = authenticate_reddit('config.ini')
subreddit = reddit_instance.subreddit('canucks')

submission = reddit_instance.submission(id='1g1swzp')

post_data = {
        "comment_id": submission.id, 
        "author": submission.author,
        "utc_created": submission.created_utc, 
        "comments": []
        }
top_level_comments = []
comment_map = {}

print(submission.title)
submission.comments.replace_more(limit=None)
comment_queue = submission.comments[:] # type: ignore

while comment_queue:
    comment = comment_queue.pop(0)
    comment_dict = {
        "comment_id": comment.id, 
        "author": str(comment.author), 
        "body": comment.body, 
        "utc_created": comment.created_utc, 
        "replies": []
        }
    
    comment_map[comment.id] = comment_dict

    if comment_dict and comment.parent_id.startswith("t1_"):
        parent_id = comment.parend_id[3:]
        top_level_comments.append(comment)

for comment in top_level_comments:
    print(comment.body)