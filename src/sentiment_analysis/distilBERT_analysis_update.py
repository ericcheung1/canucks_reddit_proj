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
    all_posts = Post.objects() # type: ignore
    total_posts = all_posts.count()
    print(f"There are {total_posts} in the the database.")

    distilbert_pipeline = pipeline(
        task="sentiment-analysis", 
        model="distilbert-base-uncased-finetuned-sst-2-english",
        truncation=True
        )


    processed_count = 0
    updated_count = 0

    for post in all_posts:
        print(f"Processing {processed_count + 1}/{total_posts} posts.")
        sentiment_result = calculate_distilbert_scores(post, distilbert_pipeline)

        if not sentiment_result:
            print(f"No comments found or processed for ID {post.post_id}")
            processed_count += 1
            continue

        sentiment_result_by_id = {
            item["comment_id"]: item
            for item in sentiment_result
            }
        
        # print(sentiment_result_by_id)

        def update_sentiment_helper(item_obj, result_map):
            if hasattr(item_obj, "comment_id") and item_obj.comment_id in result_map:
                result = result_map[item_obj.comment_id]
                item_obj.distilbert_sentiment = result["sentiment_label"]
                item_obj.distilber_confidence = result["confidence_score"]
                return True
            return False
        
        def traverse_and_update(comment_list, result_map):
            modified = False
            for item in comment_list:
                if update_sentiment_helper(item, result_map):
                    modified =  True
                if hasattr(item, "replies") and item.replies:
                    if traverse_and_update(item.replies, result_map):
                        modified = True
            return modified
        
        post_modified = traverse_and_update(post.comments, sentiment_result_by_id)

        if post_modified:
            # post.save()
            updated_count += 1
            print(f"Updated sentiment for post: {post.post_id}, {updated_count}/{total_posts}")
        else:
            print(f"No sentiment update for post: {post.post_id}")
        
        processed_count += 1

    print(f"\n --- Script Finished ---")
    print(f"Total posts updated: {updated_count}")
    print(f"Total posts processed: {processed_count}")

    disconnect()

if __name__ == "__main__":
    main()