import os
from authenticate import authenticate_reddit
import pandas as pd

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Project Root: {project_root}")

reddit_instance = authenticate_reddit('config.ini')
subreddit = reddit_instance.subreddit('canucks')
sub_id = "1g1swzp"

def fetch_comments(reddit, submission_id):
    submission = reddit.submission(id=submission_id)
    post_data = {
            "post_id": submission.id, 
            "title": submission.title,
            "author": submission.author,
            "utc_created": submission.created_utc, 
            "comments": []
            }
    comment_map = {}

    print(submission.title)
    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:] # type: ignore

    while comment_queue:
        comment = comment_queue.pop(0)
        # print(f"comment: {comment.body}")
        # extract current comment in queue's info as a dict
        comment_dict = {    
            "comment_id": comment.id, 
            "author": str(comment.author), 
            "body": comment.body, 
            "utc_created": comment.created_utc, 
            "replies": []
            }
        
        # places current comment into comment_map dict
        # by having comment_id be the key and whole comment_dict as the value
        comment_map[comment.id] = comment_dict 

        # if comment exists and is a reply
        # because replies have parent id prefixed with "t1_"
        if comment_dict and comment.parent_id.startswith("t3_"): 
            post_data["comments"].append(comment_dict)
        else:

            # assigns parent id variable which
            # is the parent submission's id
            # also strips "t1_" prefix
            parent_id = comment.parent_id[3:]
            # print(f"parent id: {parent_id}")

            if parent_id in comment_map: 
                # if parent id is submission id
                # append it as a reply in comment map
                comment_map[parent_id]["replies"].append(comment_dict)
        comment_queue.extend(comment.replies)
    
    return post_data
            
print(f"Post data: {fetch_comments(reddit_instance, sub_id)}")