import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import pandas as pd
import datetime as dt

def sentiment_distribution(all_post_obj):
    VADER_POS = [post.pos_count for post in  all_post_obj]
    VADER_NEU = [post.neu_count for post in all_post_obj]
    VADER_NEG = [post.neg_count for post in all_post_obj]
    Distil_POS = [post.distilbert_pos_count for post in all_post_obj]
    Distil_NEG = [post.distilbert_neg_count for post in all_post_obj]
    UTC_CREATED = [post.utc_created for post in all_post_obj]

    df = pd.DataFrame({"D_POS": Distil_POS, "D_NEG": Distil_NEG, "UTC": UTC_CREATED,
                       "V_POS": VADER_POS, "V_NEU": VADER_NEU, "V_NEG": VADER_NEG})
    df["UTC"] = pd.to_datetime(df["UTC"], unit="s",utc=True)
    df["Local_time"] = df["UTC"].dt.tz_convert("America/Los_Angeles")

    fig = make_subplots(rows=1, cols=2, shared_xaxes=True, shared_yaxes=True, subplot_titles=("VADER", "DistilBERT"))

    fig.add_trace(go.Scatter(x=df["Local_time"], y=df["V_POS"], name="VADER Positive", 
                             line=dict(color="#00843D", width=2.5, dash="dashdot")), row=1, col=1)
    
    fig.add_trace(go.Scatter(x=df["Local_time"], y=df["V_NEU"], name="VADER Neutral", 
                             line=dict(color="#FFB81C", width=2.5, dash="dashdot")), row=1, col=1)
    
    fig.add_trace(go.Scatter(x=df["Local_time"], y=df["V_NEG"], name="VADER Negative", 
                             line=dict(color="#D2001C", width=2.5, dash="dashdot")), row=1, col=1)
    


    fig.add_trace(go.Scatter(x=df["Local_time"], y=df["D_POS"], name="DistilBERT Positive", 
                             line=dict(color="#00843D", width=2.5, dash="dashdot")), row=1, col=2)
    
    fig.add_trace(go.Scatter(x=df["Local_time"], y=df["D_NEG"], name="DistilBERT Negative", 
                             line=dict(color="#D2001C", width=2, dash="dashdot")), row=1, col=2)

    fig.update_layout(height=675)

    return pio.to_html(fig, full_html=False)