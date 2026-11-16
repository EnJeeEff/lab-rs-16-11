from app import farewell, greet
from utils import add, multiply


def test_greet():
    assert greet("Git") == "Hello, Git!"


def test_farewell():
    assert farewell("Git") == "Goodbye, Git!"


def test_utils():
    assert add(2, 3) == 5
    assert multiply(2, 3) == 6