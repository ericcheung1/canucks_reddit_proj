from mongoengine import connect, disconnect
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_root)
if project_root not in sys.path:
    sys.path.append(project_root)

from web_app.models import Post, Comment, Reply
import pandas as pd
import datetime as dt
import configparser
import plotly.graph_objects as go

def connect_Mongo():
    config = configparser.ConfigParser()
    config.read(os.path.join(project_root, "config.ini"))

    Mongo_uri = None
    if config.has_section("MongoDB") and config.has_option("MongoDB", "uri"):
        Mongo_uri = config.get("MongoDB", "uri")
        print("Connecting to Local MongoDB via config.ini")
    else:
        raise ValueError("Error in Connecting to MongoDB")

    MONGODB_SETTINGS = {
        "host": Mongo_uri,
        "db": "canucks_reddit_data"
    }

    return connect(host=MONGODB_SETTINGS["host"], db=MONGODB_SETTINGS["db"])
