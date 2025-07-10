import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import pandas as pd
import datetime as dt

def draw_pie_chart(all_post_obj):
    VADER_POS = [post.pos_count for post in  all_post_obj]
    VADER_NEU = [post.neu_count for post in all_post_obj]
    VADER_NEG = [post.neg_count for post in all_post_obj]
    Distil_POS = [post.distilbert_pos_count for post in all_post_obj]
    Distil_NEG = [post.distilbert_neg_count for post in all_post_obj]

    df = pd.DataFrame({"D_POS": Distil_POS, "D_NEG": Distil_NEG, "V_POS": VADER_POS, 
                       "V_NEU": VADER_NEU, "V_NEG": VADER_NEG})
    
    v_colors = ["#00843D", "#FFB81C", "#D2001C"]
    d_colors = ["#00843D", "#D2001C"]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

    fig.add_trace(go.Pie(labels=["Positive Comments", "Neutral Comments", "Negative Comments"],
                        values=[sum(df["V_POS"]), sum(df["V_NEU"]), sum(df["V_NEG"])], 
                        marker_colors=v_colors), row=1, col=1)
    
    fig.add_trace(go.Pie(labels=["Positive Comments", "Negative Comments"],
                        values=[sum(df["D_POS"]), sum(df["D_NEG"])], 
                        marker_colors=d_colors), row=1, col=2)
    
    fig.update_traces(hole=.4, hoverinfo="label+percent")

    fig.update_layout(
        annotations=[dict(text='VADER', x=sum(fig.get_subplot(1, 1).x) / 2, y=0.5, # type: ignore
                        font_size=20, showarrow=False, xanchor="center"),
                        dict(text='DistilBERT', x=sum(fig.get_subplot(1, 2).x) / 2, y=0.5, # type: ignore
                        font_size=20, showarrow=False, xanchor="center")],
                        height=675)
    
    fig.update(layout_showlegend=False)
    
    return pio.to_html(fig, full_html=False)
