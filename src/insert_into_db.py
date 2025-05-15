from pymongo import MongoClient
from get_comments import fetch_comments
from authenticate import authenticate_reddit, connect_mongodb

reddit_instance = authenticate_reddit("config.ini")
comment_forest = fetch_comments(reddit_instance, "1g677aq")

client = connect_mongodb("config.ini")

db = client['test_db']
post_collection = db['posts']

try:
    inserted_result = post_collection.insert_one(comment_forest)
    print(f"Successfully inserted post with ID: {inserted_result.inserted_id}")
except Exception as e:
    print(f"Error in inserting: {e}")

client.close()