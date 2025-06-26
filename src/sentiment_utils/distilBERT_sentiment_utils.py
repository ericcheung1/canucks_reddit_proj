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
        comment_list = []
        comment_helper(Game_post.comments, comment_list)
        return comment_list

def calculate_distilbert_scores(Game_post, distilbert_analyzer):

    scores_dict = {
        "sentiment_label": [],
        "confidence_score": [],
        "comment_id": []
        }

    comment_list = flatten_list(Game_post)

    for comment in comment_list:
        distilbert_result = distilbert_analyzer(comment["body"])
        scores_dict["sentiment_label"].append(distilbert_result[0]["label"])
        scores_dict["confidence_score"].append(distilbert_result[0]["score"])
        scores_dict["comment_id"].append(comment["comment_id"])


    return scores_dict