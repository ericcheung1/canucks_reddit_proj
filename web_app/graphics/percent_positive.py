import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import datetime as dt

def create_pct_pos_graph(all_post_obj):
    VADER_POS = [post.pos_count for post in  all_post_obj]
    BERT_POS = [post.distilbert_pos_count for post in all_post_obj]
    UTC_CREATED = [post.utc_created for post in all_post_obj]
    TOTAL_COMMENTS = [post.total_bodies for post in all_post_obj]
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
        xaxis=dict(title=dict(text="Time")),
        yaxis=dict(title=dict(text="Percentage of Positive Comments"),
                tickformat=".0%"),
        height=675,
    )
    
    return pio.to_html(fig, full_html=False)