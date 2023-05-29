import pytest
import requests

def testSub():
    data = {"a": 2.5, "b": 5.0}
    response = requests.post("http://127.0.0.1:8000/sub", json=data)
    assert response.status_code == 200

def testMult():
    data = {"a": 2.5, "b": 5.0}
    response = requests.post("http://127.0.0.1:8000/mult", json=data)
    assert response.status_code == 200

def testDiv1():
    data = {"a": 5.0, "b": 2.0}
    response = requests.post("http://127.0.0.1:8000/div", json=data)
    assert response.status_code == 200

def testDiv2():
    data = {"a": 5.0, "b": 0}
    response = requests.post("http://127.0.0.1:8000/div", json=data)
    assert response.status_code == 400