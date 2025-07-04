from flask import Blueprint, render_template, url_for
from .models import Post, Comment, Reply
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import datetime as dt

bp = Blueprint("main", __name__)

@bp.route('/')
def index():
    return render_template("home_page.html")

@bp.route('/posts')
def list_posts():
    all_posts = Post.objects().only( # type: ignore
        'title', 'post_id', "total_bodies", 
        "pos_count", "distilbert_pos_count", "utc_created") 
    
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
                mode="lines",
                name="VADER",
                line=dict(width=2)))

    fig.add_trace(
        go.Scatter(x=df["Local_time"], y=df["BERT_PCT"],
                mode="lines",
                name="DistilBERT",
                line=dict(width=2)))

    fig.update_layout(
        title=dict(text="Percentage of Positive Comments in VADER vs. DistilBERT"),
        xaxis=dict(title=dict(text="Time")),
        yaxis=dict(title=dict(text="Percentage of Positive Comments"),
                tickformat=".0%"),
        height=675,
    )
    chart_html = pio.to_html(fig, full_html=False)
    return render_template("list_posts.html", posts=all_posts, chart=chart_html)

@bp.route('/posts/<string:post_id>')
def post_detail(post_id):
    post = Post.objects(post_id=post_id).first() # type: ignore
    post_title = post.title.replace("Post Game Thread: ", "")

    if post:
        return render_template("post_detail.html", post=post, clean_title=post_title)
    else:
        return "Post Not Found!", 404
