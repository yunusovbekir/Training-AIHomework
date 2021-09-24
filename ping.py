from json import JSONDecodeError
from logging import getLogger
from requests import get
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
logger = getLogger('werkzeug')


@api.route('/api/v1/ping')
class Ping(Resource):

    @ns.doc("Make GET request to the given URL")
    def post(self):
        """
            This API endpoint accepts json object which has the key "url".
            Makes a GET request to the given URL and
            returns the response of the request.
            Example: {"url": "http://ReceiverService:8080/api/v1/info"}
            :return: dict or error message as string
        """
        try:
            data = api.payload
            response = get(data.get('url'))
            return response.json()
        except AttributeError:
            # if request payload is empty,
            # we return user-friendly error message
            return "Invalid payload data", 400
        except JSONDecodeError:
            # if response from the given URL is not JSON,
            # we return user-friendly error message
            return "URL doesn't return JSON object", 400


@api.route('/health')
class HealthCheck(Resource):

    @ns.doc('Health check API endpoint')
    def get(self):
        """
            Health check API endpoint.
            If server works well, it returns 200 healthy.
            :return: string
        """
        logger.info("200 - (healthy)")
        return "200 - (healthy)"


if __name__ == '__main__':
    app.run()
