from transformers import pipeline # type: ignore

def comment_helper(comment_or_reply, all_bodies):
    for item in comment_or_reply:
        if item.body and item.body != "[deleted]":
            all_bodies.append({"comment_id": item.comment_id, "body": item.body})
        if item.replies:
            comment_helper(item.replies, all_bodies)


def flatten_list(Game_post):
    if not Game_post:
        return []
    else:
        all_text_bodies = []
        comment_helper(Game_post.comments, all_text_bodies)
        return all_text_bodies

def calculate_distilbert_scores(Game_post, distilbert_analyzer):

    scores_dict = {
        "sentiment_label": [],
        "confidence_score": []
        }

    all_text_bodies = flatten_list(Game_post)

    for body in all_text_bodies:
        distilbert_result = distilbert_analyzer(body)
        scores_dict["sentiment_label"].append(distilbert_result[0]["label"])
        scores_dict["confidence_score"].append(distilbert_result[0]["score"])


    return scores_dict