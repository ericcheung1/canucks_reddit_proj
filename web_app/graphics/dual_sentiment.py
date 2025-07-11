import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import pandas as pd
import datetime as dt

def sentiment_distribution(all_post_obj):
    total_comments = [post.total_bodies for post in all_post_obj]
    UTC_CREATED = [post.utc_created for post in all_post_obj]
    post_title = [post.title for post in all_post_obj]

    df = pd.DataFrame({"UTC": UTC_CREATED, "title": post_title, "total_comments": total_comments})
    df["UTC"] = pd.to_datetime(df["UTC"], unit="s",utc=True)
    df["Local_time"] = df["UTC"].dt.tz_convert("America/Los_Angeles")

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df["Local_time"], y=df["total_comments"], 
                             line_shape="hvh", line = dict(color='#000000', width=2.5)))

    fig.update_layout(
        xaxis=dict(
            title=dict(text="2024-25 NHL Season")),
        yaxis=dict(
            title=dict(text="# of Comments")
        ), 
        height=675)

    return pio.to_html(fig, full_html=False)