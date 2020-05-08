from flask import Blueprint
from flask import render_template, url_for, request
from myblog.models import Post

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    image_file = url_for('static', filename='default.png')
    return render_template('index.html', posts=posts, image_file=image_file)


@main.route('/about')
def about():
    image_file = url_for('static', filename='default.png')
    return render_template('about.html', title='About', image_file=image_file)