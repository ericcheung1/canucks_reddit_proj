from web_app.models import Post, Comment, Reply
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def comment_helper(comment_or_reply, all_bodies):
    for item in comment_or_reply:
        if item.body and item.body != "[deleted]":
            all_bodies.append(item.body)
        if item.replies:
            comment_helper(item.replies, all_bodies)


def flatten_list(Game_post):
    if not Game_post:
        return []
    else:
        all_text_bodies = []
        comment_helper(Game_post.comments, all_text_bodies)
        return all_text_bodies
    
def vader_analyser(all_text_list, sia):

    comment_score_dict = {
    "compound" : [],
    "neg" : [],
    "neu" : [],
    "pos" : []
    }
    for body in all_text_list:
        vader_score = sia.polarity_scores(body)
        comment_score_dict['neg'].append(vader_score['neg'])
        comment_score_dict['neu'].append(vader_score['neu'])
        comment_score_dict['pos'].append(vader_score['pos'])
        comment_score_dict['compound'].append(vader_score['compound'])
    
    return comment_score_dict

def calculate_vader_scores(Game_post, sia):
    all_text_bodies = flatten_list(Game_post)
    total_bodies = len(all_text_bodies)

    if not all_text_bodies:
        return {
            "Average_Neg": 0, 
            "Average_Neu": 0, 
            "Average_Pos": 0, 
            "Average_Compound": 0,
            "Total_Neg": 0,
            "Total_Neu": 0,
            "Total_Pos": 0,
            "Total_Comments": 0
        }

    vader_scores = vader_analyser(all_text_bodies, sia)

    avg_neg = sum(vader_scores['neg'])/total_bodies
    avg_neu = sum(vader_scores['neu'])/total_bodies
    avg_pos = sum(vader_scores['pos'])/total_bodies
    avg_compound = sum(vader_scores['compound'])/total_bodies

    neg_count = 0
    neu_count = 0
    pos_count = 0

    for compound_score in vader_scores["compound"]:
        if compound_score >= 0.05:
            pos_count += 1
        elif compound_score <= -0.05:
            neg_count += 1
        else:
            neu_count += 1

    return {
            "Average_Neg": avg_neg, 
            "Average_Neu": avg_neu, 
            "Average_Pos": avg_pos, 
            "Average_Compound": avg_compound,
            "Total_Neg": neg_count,
            "Total_Neu": neu_count,
            "Total_Pos": pos_count,
            "Total_Comments": total_bodies
        }

