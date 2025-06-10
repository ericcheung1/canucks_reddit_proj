from web_app.models import Post, Comment, Reply
from web_app import create_app
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def comment_recursive(comment_or_reply, all_bodies):
    for item in comment_or_reply:
        if item.body and item.body != "[deleted]":
            all_bodies.append(item.body)
        if item.replies:
            comment_recursive(item.replies, all_bodies)


def body_list(Game_post):
    if not Game_post:
        return []
    else:
        all_text_bodies = []
        comment_recursive(Game_post.comments, all_text_bodies)
        return all_text_bodies
    
def vader_analyser(all_text_list):
    sia = SentimentIntensityAnalyzer()

    score_dict = {
    "compound" : [],
    "neg" : [],
    "neu" : [],
    "pos" : []
    }
    for body in all_text_list:
        vader_score = sia.polarity_scores(body)
        score_dict['neg'].append(vader_score['neg'])
        score_dict['neu'].append(vader_score['neu'])
        score_dict['pos'].append(vader_score['pos'])
        score_dict['compound'].append(vader_score['compound'])
    
    return score_dict


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        print("DB Connected:")
        sample_post = Post.objects(post_id="1g677aq").first() # type: ignore

        if sample_post:
            print(f"Title: {sample_post.title}")
            List_of_bodies = body_list(sample_post)
            print(f"Extracted {len(List_of_bodies)} comment/reply bodies.") # type: ignore
            # print("\n".join(List_of_bodies[:5]))
        else:
            print("Choose another game?")

        scores = vader_analyser(List_of_bodies)

        print(scores['compound'])
    
    print("DB Closed For testing")

