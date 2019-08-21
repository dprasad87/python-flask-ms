from flask import request
from flask_restplus import Resource
from api.restplus import api

import api.blog.serializers as serializers
import api.blog.business as business


ns = api.namespace("blog/posts", description='Operations related to blog posts')


@ns.route('/')
class PostCollection(Resource):

    @api.expect(serializers.blog_post)
    def post(self):
        """Creates a new blog post"""
        business.create_blog_post(request.json)
        return None, 201

@ns.route('/<int:id>')
@api.response('404', 'Page not found')
class PostItem(Resource):

    @api.marshal_with(serializers.blog_post)
    def get(self, id):
        """
        returns a blog post
        """
        # call model in database
        return business.get_blog_post(id)

        # return {"hello": id }

    def put(self, id):
        """
        Updates a blog post
        """
        pass