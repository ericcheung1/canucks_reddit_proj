from web_app.models import Post, Comment, Reply
from transformers import pipeline # type: ignore

def comment_helper(comment_or_reply, all_bodies):
    for item in comment_or_reply:
        if item.body and item.body != "[deleted]":
            all_bodies.append(item.body)
        if item.replies:
            comment_helper(item.replies, all_bodies)


def flatten_list(Game_post):
    if not Game_post:
        return []
    else:
        all_text_bodies = []
        comment_helper(Game_post.comments, all_text_bodies)
        return all_text_bodies

def distilbert_analyzer(all_text_bodies, sentiment_analyzer):

    scores_dict = {
        "sentiment_label": [],
        "confidence_score": []
        }


sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
result = sentiment_analyzer("The dedication of these guys is insane. It took me three weeks and two reminders to only finish my resume")
print(result)