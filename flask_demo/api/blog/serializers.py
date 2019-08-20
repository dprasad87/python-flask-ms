from flask_restplus import fields

from api.restplus import api

blog_post = api.model('Blog post', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog post'),
    'title': fields.String(required=True),
    'body': fields.String(required=True),
    'pub_date': fields.DateTime
})