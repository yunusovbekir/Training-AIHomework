from ping import app
from pytest import fixture
from json import dumps


@fixture
def client():
    """
    Configures the app for testing
    Sets app config variable ``TESTING`` to ``True``
    :return: App for testing
    """

    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_ping_invalid_data(client):
    response = client.post(path='/api/v1/ping')
    assert response.status_code == 400
    assert response.json == 'Invalid payload data'


def test_ping_invalid_url(client):
    payload = dumps({"url": "http://google.com"})
    response = client.post(
        path='/api/v1/ping',
        headers={"Content-Type": "application/json"},
        data=payload,
    )
    assert response.status_code == 400
    assert response.json == "URL doesn't return JSON object"


def test_ping_successful(client):
    payload = dumps({"url": "https://jsonplaceholder.typicode.com/todos/1"})
    response = client.post(
        path='/api/v1/ping',
        headers={"Content-Type": "application/json"},
        data=payload,
    )
    assert response.status_code == 200


def test_health(client):
    response = client.get(path='/health')
    assert response.status_code == 200
