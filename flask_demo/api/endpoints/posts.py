import logging

from flask_restplus import Resource

from flask_demo.api.restplus import api
from flask_demo.database.models import Post

log = logging.getLogger(__name__)
ns = api.namespace('blog/posts', description='Operation related to blog posts')

@ns.route('/<int:id>')
@api.response('404', 'Page not found')
class PostItem(Resource):

    def get(self, id):
        """
        :return: a blog post
        """
        # call model in database
        return Post.query.filter(Post.id == id).one()