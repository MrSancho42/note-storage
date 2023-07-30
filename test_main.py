import requests
import main

base_url = "http://127.0.0.1:8000"


def test_function():
    assert main.root() == {'message': 'Hello World'}


def test_response():
    assert requests.get(base_url).json() == {'message': 'Hello World'}
