from pymongo import MongoClient
from get_comments import fetch_comments
from authenticate import authenticate_reddit, connect_mongodb

reddit_instance = authenticate_reddit("config.ini")
comment_forest = fetch_comments(reddit_instance, "1gg714l")

client = connect_mongodb("config.ini")

def insert_posts(client, database, collection, post_data):
    post_id = post_data["post_id"]
    db = client[database]
    collection = db[collection]
    exists = collection.find_one( { "post_id" : f"{post_id}" } )


    if exists == None:
        try:
            inserted_result = collection.insert_one(post_data)
            print(f"Successfully inserted post with ID: {inserted_result.inserted_id}")
            return inserted_result
        except Exception as e:
            print(f"Error in inserting: {e}")
            return None
    else:
        print("Post is Already in Collection.")
        return None

insert_posts(client, "test_db", "posts", comment_forest)

client.close()