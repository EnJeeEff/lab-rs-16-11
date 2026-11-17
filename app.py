def greet(name, greeting="Hello"):
    return f"{greeting}, {name.strip()}!"


def farewell(name):
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))