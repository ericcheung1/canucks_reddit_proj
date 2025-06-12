from nltk.sentiment.vader import SentimentIntensityAnalyzer
from mongoengine import connect, disconnect
import configparser
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_root)
if project_root not in sys.path:
    sys.path.append(project_root)

from web_app.models import Post
from vader_sentiment_utils import calculate_vader_scores

def main():

    config = configparser.ConfigParser()
    config.read(os.path.join(project_root, "config.ini"))

    mongo_host = config.get("MongoDB", "server")
    mongo_db_name = config.get("MongoDB", "database")

    connect(db=mongo_db_name, host=mongo_host)

    print(f"Connect to MongoDB and using {mongo_db_name} database")

    all_posts = Post.objects() # type: ignore
    total_posts = all_posts.count()
    print(f"There are {total_posts} posts in the database")

    disconnect()
    print(f"MongoDB Connection Disconnected")


if __name__ == "__main__":
    main()