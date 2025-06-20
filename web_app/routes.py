from flask import Blueprint, render_template, url_for
from .models import Post, Comment, Reply

bp = Blueprint("main", __name__)

@bp.route('/')
def index():
    return f'<h1>Welcome to Canucks Sentiment Analysis! Home Page Coming Soon! Checkout the Posts Below!</h1><p><a href="{url_for("main.list_posts")}">View All Posts</a></p>'

@bp.route('/posts')
def list_posts():
    all_posts = Post.objects().only('title', 'post_id') # type: ignore
    return render_template("list_posts.html", posts=all_posts)

@bp.route('/posts/<string:post_id>')
def post_detail(post_id):
    post = Post.objects(post_id=post_id).first() # type: ignore
    post_title = post.title.replace("Post Game Thread: ", "")

    if post:
        return render_template("post_detail.html", post=post, clean_title=post_title)
    else:
        return "Post Not Found!", 404
