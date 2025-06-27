from transformers import pipeline # type: ignore

def comment_helper(comment_or_reply, all_bodies):
    for item in comment_or_reply:
        if item.body and item.body != "[deleted]":
            all_bodies.append({"comment_id": item.comment_id, "body": item.body})
        if item.replies:
            comment_helper(item.replies, all_bodies)


def flatten_list(Game_post):
    if not Game_post or not Game_post.comments:
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

    comment_items = flatten_list(Game_post)

    comment_bodies = [item["body"] for item in comment_items]
    comment_ids = [item["comment_id"] for item in comment_items]

    results_list = []

    if not comment_bodies:
        return results_list

    distilbert_results = distilbert_analyzer(comment_bodies)

    for i, value in enumerate(distilbert_results):
        results_list.append({
            "comment_id": comment_ids[i],
            "sentiment_label": value["label"],
            "confidence_score": value["score"]
        })

    return results_list