from flask import Blueprint, render_template, url_for
from .models import Post, Comment, Reply
from .graphics.dual_sentiment import sentiment_distribution
from .graphics.percent_positive import create_pct_pos_graph

bp = Blueprint("main", __name__)

@bp.route('/')
def index():
    return render_template("home_page.html")

@bp.route('/posts')
def list_posts():
    all_posts = Post.objects().only( # type: ignore
        'title', 'post_id', "total_bodies", 
        "pos_count", "neu_count", "neg_count","utc_created",
        "distilbert_pos_count", "distilbert_neg_count") 
    chart1 = sentiment_distribution(all_posts)
    chart2 = create_pct_pos_graph(all_posts)
    return render_template("list_posts.html", posts=all_posts, 
                           chart_one=chart1, chart_two = chart2)

@bp.route('/posts/<string:post_id>')
def post_detail(post_id):
    post = Post.objects(post_id=post_id).first() # type: ignore
    post_title = post.title.replace("Post Game Thread: ", "")

    if post:
        return render_template("post_detail.html", post=post, clean_title=post_title)
    else:
        return "Post Not Found!", 404
    
@bp.route('/visualiztions')
def draw_graphs():
    all_posts = Post.objects() 

    return "<h2>In Progress!</h2>"
