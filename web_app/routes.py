from flask import Blueprint, render_template, url_for
from .models import Post

bp = Blueprint("main", __name__)

@bp.route('/')
def index():
    return f'<h1>Welcome to the Canucks Reddit Data!</h1><p><a href="{url_for("main.list_posts")}">View All Posts</a></p>'

@bp.route('/posts')
def list_posts():
    all_posts = Post.objects().only('title', 'post_id') # type: ignore
    return render_template("list_posts.html", posts=all_posts)

@bp.route('/posts/<string:post_id>')
def post_detail(post_id):
    post = Post.objects(post_id=post_id).first() # type: ignore

    if post:
        return render_template("post_detail.html", post=post)
    else:
        return "Post Not Foun!", 404
