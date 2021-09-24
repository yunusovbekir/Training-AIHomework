from flask import Flask, scaffold, helpers

# fix import error in flask
helpers._endpoint_from_view_func = scaffold._endpoint_from_view_func

from flask_restplus import Resource, Api    # noqa E402

app = Flask(__name__)
api = Api(app)
ns = api.namespace(
    'Engineering Assignment',
    description='API documentation description'
)


@api.route('/api/v1/info')
class Receiver(Resource):

    @ns.doc('API endpoint to return static data')
    def get(self):
        return {"Receiver": "Cisco is the best!"}


if __name__ == '__main__':
    app.run()
