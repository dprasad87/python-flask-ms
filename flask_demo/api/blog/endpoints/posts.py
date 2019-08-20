from flask_restplus import Resource

from api.restplus import api

ns = api.namespace("blog/posts", description='Operations related to blog posts')


@ns.route('/<int:id>')
@api.response('404', 'Page not found')
class PostItem(Resource):

    def get(self, id):
        """
        :return: a blog post
        """
        # call model in database
        # return Post.query.filter(Post.id == id).one()
        return {"hello": "world"}
