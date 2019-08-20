import logging

from database import db
from database.models import Post

log = logging.getLogger(__name__)

def create_blog_post(data):
    log.info(">>> create_blog_post invoked")
    print(">>> create_blog_post invoked")
    title = data.get('title')
    body = data.get('body')
    post = Post(title, body)
    db.session.add(post)
    db.session.commit()

def get_blog_post(id):
    return Post.query.filter(Post.id == id).one()