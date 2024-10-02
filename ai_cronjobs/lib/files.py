import os


def read_text(path):
    if os.path.exists(path):
        with open(path, "r") as file:
            return file.read().strip()
    return None


def store_text(path, text):
    with open(path, "w") as file:
        file.write(str(text))
