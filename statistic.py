import os
import unicodedata


def chinese():
    chinese_count = 0
    chinese_word = set()

    for filename in os.listdir("./real_captcha"):
        color, text, *_ = filename[:-4].split("_")
        for c in text:
            if 'CJK' in unicodedata.name(c):
                chinese_count += 1
                chinese_word.add(c)

    return len(chinese_word), chinese_count, chinese_word


def simulate(word_count, chinese_count):
    import random
    s = [i for i in range(word_count)]
    chinese_word = set()
    for _ in range(chinese_count):
        chinese_word.add(random.choice(s))
    return len(chinese_word)


length, count, word = chinese()
print(length, simulate(700, count))

with open("./font/chinese7000.txt", encoding="utf-8") as f:
    word_list = [i for i in f.readline()]

print(sorted(word_list.index(w) for w in word))