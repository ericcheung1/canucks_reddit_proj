from flask import Blueprint, render_template, url_for
from .models import Post, Comment, Reply
from .graphics.dual_sentiment import sentiment_distribution
from .graphics.sentiment_proportions import draw_pie_chart

bp = Blueprint("main", __name__)

@bp.route('/')
def index():
    return render_template("home_page.html")

@bp.route('/posts')
def list_posts():
    all_posts = Post.objects().only( # type: ignore
        'title', 'post_id', "total_bodies", 
        "vader_post_classification", "distilbert_post_classification")
    
    return render_template("list_posts.html", posts=all_posts)

@bp.route('/posts/<string:post_id>')
def post_detail(post_id):
    post = Post.objects(post_id=post_id).first() # type: ignore
    post_title = post.title.replace("Post Game Thread: ", "")

    if post:
        return render_template("post_detail.html", post=post, clean_title=post_title)
    else:
        return "Post Not Found!", 404
    
@bp.route('/visualize')
def draw_graphs():
    all_posts = Post.objects().only('title', 'post_id', "total_bodies", # type: ignore
        "pos_count", "neu_count", "neg_count","utc_created",
        "distilbert_pos_count", "distilbert_neg_count") 
    
    chart1 = sentiment_distribution(all_posts)
    chart2 = draw_pie_chart(all_posts)
    return render_template("visualizations.html", chart_one=chart1, chart_two = chart2)
