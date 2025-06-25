from nltk.sentiment.vader import SentimentIntensityAnalyzer
from mongoengine import disconnect
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(project_root)
if project_root not in sys.path:
    sys.path.append(project_root)

from web_app.models import Post, Comment, Reply
from src.sentiment_utils.vader_sentiment_utils import calculate_vader_scores

def main():
    all_posts = Post.objects() # type: ignore
    total_posts = all_posts.count()
    print(f"There are {total_posts} posts in the database.")

    sia = SentimentIntensityAnalyzer()

    processed_count = 0
    updated_count = 0

    for post in all_posts:
        scores = calculate_vader_scores(post, sia)
        processed_count += 1

        print(f"Processing {processed_count}/{total_posts}")

        post.avg_neg = scores["Average_Neg"]
        post.avg_neu = scores["Average_Neu"]
        post.avg_pos = scores["Average_Pos"]
        post.avg_compound = scores["Average_Compound"]
        post.neg_count = scores["Total_Neg"]
        post.neu_count = scores["Total_Neu"]
        post.pos_count = scores["Total_Pos"]
        post.total_bodies = scores["Total_Comments"]


        def calculate_individual_score(game_post_comments):
            for comment in game_post_comments:
                
                if comment.body and comment.body != "[deleted]":
                    score_for_individual = sia.polarity_scores(comment.body)
                    comment.neg_sentiment = score_for_individual["neg"]
                    comment.pos_sentiment = score_for_individual["pos"]
                    comment.neu_sentiment = score_for_individual["neu"]
                    comment.compound_sentiment = score_for_individual["compound"]
                else:
                    comment.neg_sentiment = 0.0
                    comment.pos_sentiment = 0.0
                    comment.neu_sentiment = 0.0
                    comment.compound_sentiment = 0.0

                if comment.replies:
                    calculate_individual_score(comment.replies)
        
        calculate_individual_score(post.comments)

        # post.save()
        updated_count += 1

    disconnect()
    print(f"Successfully updated {updated_count} out of {processed_count} posts.")
    print(f"MongoDB Connection Disconnected.")


if __name__ == "__main__":
    main()