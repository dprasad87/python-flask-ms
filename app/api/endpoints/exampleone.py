from flask import jsonify, make_response
from flask_restplus import Resource, Namespace, fields

example_one_namespace = Namespace('exampleone', description='Example API one')

@example_one_namespace.route("/")
class ExampleEndpoint(Resource):

    @staticmethod
    def __success(payload):
        return jsonify({
            "status": True,
            "payload": payload
        })

    @staticmethod
    def __failure(errors):
        return jsonify({
            "status": False,
            "payload": errors
        })

    @example_one_namespace.doc(responses={200: 'OK',
                                          500: 'Internal Server Error'})

    def get(self):
        return make_response(self.__success([]), 200)

    model = example_one_namespace.model("arguments", {
        "arg": fields.String(required=True)
    })