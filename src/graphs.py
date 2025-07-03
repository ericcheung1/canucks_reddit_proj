from mongoengine import disconnect
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_root)
if project_root not in sys.path:
    sys.path.append(project_root)

from web_app.models import Post, Comment, Reply
import pandas as pd
import datetime

all_posts = Post.objects().only( # type: ignore
    'title', 'post_id', "total_bodies", 
    "pos_count", "distilbert_pos_count",
    "utc_created"
    )

for post in all_posts:
    print(f"\nVADER Postive: {post.pos_count}")
    print(f"DistilBERT Postive: {post.distilbert_pos_count}")
    print(f"UTC: {datetime.datetime.fromtimestamp(post.utc_created)}")

df = pd.DataFrame({"VADER": all_posts.pos_count, 
              "DistilBERT": all_posts.distilbert_pos_count,
              "UTC": all_posts.utc_created})
print(df.head())

disconnect()