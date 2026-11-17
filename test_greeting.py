from app import greet


def test_custom_greeting():
    assert greet("Git", "Hi") == "Hi, Git!"
    assert greet("Мир", "Привет") == "Привет, Мир!"