def get_input(filename):
    """Gets input of all wordle words and gets array of words"""
    with open(filename, "r") as f:
        words = f.read()
        out = words.split("\n")
        return out[:-1]