def generate_contents(word_count):
    return " ".join(["word"] * word_count)

def generate_numbered_contents(word_count):
    return " ".join([f"word{i}" for i in range(1, word_count + 1)])