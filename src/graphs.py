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

connect(host=MONGODB_SETTINGS["host"], db=MONGODB_SETTINGS["db"])

all_posts = Post.objects().only( # type: ignore
    'title', 'post_id', "total_bodies", 
    "pos_count", "distilbert_pos_count",
    "utc_created"
    )
print(f"finished querying db")

VADER_POS = [post.pos_count for post in  all_posts]
BERT_POS = [post.distilbert_pos_count for post in all_posts]
UTC_CREATED = [post.utc_created for post in all_posts]
TOTAL_COMMENTS = [post.total_bodies for post in all_posts]
df = pd.DataFrame({
    "VADER": VADER_POS, "BERT": BERT_POS, 
    "UTC": UTC_CREATED, "TOTAL": TOTAL_COMMENTS})
df["UTC"] = pd.to_datetime(df["UTC"], unit="s",utc=True)
df["Local_time"] = df["UTC"].dt.tz_convert("America/Los_Angeles")
df["VADER_PCT"] = df["VADER"] / df["TOTAL"]
df["BERT_PCT"] = df["BERT"] / df["TOTAL"]
# print(df.head())

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=df["Local_time"], y=df["VADER_PCT"],
               mode="lines+markers",
               name="VADER",
               line=dict(width=2)))

fig.add_trace(
    go.Scatter(x=df["Local_time"], y=df["BERT_PCT"],
               mode="lines+markers",
               name="DistilBERT",
               line=dict(width=3)))

fig.update_layout(
    title=dict(text="Percentage of Positive Comments in VADER vs. DistilBERT"),
    xaxis=dict(title=dict(text="Time")),
    yaxis=dict(title=dict(text="Percentage of Positive Comments"),
               tickformat=".0%"),
)


fig.show()

disconnect()