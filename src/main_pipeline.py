from reddit_pipeline.authenticate import authenticate_reddit, connect_mongodb
from reddit_pipeline.get_comments import fetch_comments
from reddit_pipeline.insert_into_db import insert_posts
import pandas as pd
import logging
import time
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_root)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s   "
)

logging.info("This is an informational message.")
logging.warning("This message indicates a potential problem.")
logging.error("This message indicates a serious error.")
logging.critical("This message indicates a critical error which might lead to program termination")

post_ids = pd.read_csv(os.path.join(project_root, "data", "post_ids.csv"))
reddit_instance = authenticate_reddit("config.ini")
client = connect_mongodb("config.ini")
database = "canucks_reddit_data"
collection = "post_game_threads"

for index, data in post_ids.iterrows():
    db = client[database]
    post_collection = db[collection]
    exists = post_collection.find_one( { "post_id" : f"{data["post_id"]}" } )

    if exists:
        logging.info(f"Post is Already in Collection")
        continue
    try:
        post_data = fetch_comments(reddit_instance, data["post_id"])
        if post_data:
            logging.info(f"Successfully retrieved post data: {post_data["title"]}")
            time.sleep(2)
            inserted = insert_posts(client, database, collection, post_data)
            if inserted:
                logging.info(f"Successfully inserted post into database: {inserted}")
        else:
            logging.warning(f"Failed to insert post data: {post_data["title"]}")
    except Exception as e:
        logging.error(f"Error in inserting process: {e}")
    

client.close()