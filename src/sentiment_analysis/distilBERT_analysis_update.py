from mongoengine import disconnect
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(project_root)
if project_root not in sys.path:
    sys.path.append(project_root)

from web_app.models import Post, Comment, Reply
from transformers import pipeline # type: ignore 
from src.sentiment_utils.distilBERT_sentiment_utils import calculate_distilbert_scores

def main():
    all_posts = Post.objects()
    total_posts = all_posts.count()
    print(f"There are {total_posts} in the the database.")

    distilbert_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    for post in all_posts:

        scores = calculate_distilbert_scores(post, distilbert_pipeline)
        scores["sentiment_label"]

        for comment in post.comments:
            
