
import random
import re
from collections import defaultdict

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

def build_5gram_model(words):
    model = defaultdict(list)
    for i in range(len(words) - 4):
        key = tuple(words[i:i+4])
        model[key].append(words[i+4])
    return model

def generate_text(model, seed, length=30):
    current = tuple(seed.lower().split())
    output = list(current)

    for _ in range(length):
        if current not in model:
            break
        next_word = random.choice(model[current])
        output.append(next_word)
        current = tuple(output[-4:])

    return ' '.join(output)

if __name__ == "__main__":
    with open("poe.txt", "r", encoding="utf-8") as f:
        text = f.read()

    words = preprocess(text)
    model = build_5gram_model(words)

    seeds = [
        "the day was very",
        "it was a dark",
        "i felt a sense"
    ]

    for s in seeds:
        print(generate_text(model, s))
