def greet(name, greeting="Hello"):
    """Вернуть приветствие для name.

    greeting - слово приветствия (по умолчанию "Hello").
    Пробелы по краям name обрезаются.
    """
    return f"{greeting}, {name.strip()}!"


def farewell(name):
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))