from flask import Blueprint
from flask import render_template
from myblog.models import Post


posts = Blueprint('posts', __name__)


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
