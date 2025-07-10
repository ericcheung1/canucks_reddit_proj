import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import pandas as pd
import datetime as dt

def sentiment_distribution(all_post_obj):
    Distil_POS = [post.distilbert_pos_count for post in all_post_obj]
    Distil_NEG = [post.distilbert_neg_count for post in all_post_obj]
    UTC_CREATED = [post.utc_created for post in all_post_obj]

    df = pd.DataFrame({"D_POS": Distil_POS, "D_NEG": Distil_NEG, "UTC": UTC_CREATED})
    df["UTC"] = pd.to_datetime(df["UTC"], unit="s",utc=True)
    df["Local_time"] = df["UTC"].dt.tz_convert("America/Los_Angeles")

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df["Local_time"], y=df["D_POS"] + df["D_NEG"], 
                             name="Total Comments", line=dict(color="#000000", width=3)))

    fig.update_layout(
        xaxis=dict(
            title=dict(text="2024-25 NHL Season")),
        yaxis=dict(
            title=dict(text="Number of Comments Per Thread")
        ), 
        height=675)

    return pio.to_html(fig, full_html=False)