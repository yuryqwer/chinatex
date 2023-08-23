import os
import unicodedata


def chinese():
    chinese_count = 0
    chinese_word = set()

    for filename in os.listdir("./real_img"):
        color, text, *_ = filename[:-4].split("_")
        for c in text:
            if 'CJK' in unicodedata.name(c):
                chinese_count += 1
                chinese_word.add(c)

    return len(chinese_word), chinese_count


def simulate(word_count, chinese_count):
    import random
    s = [i for i in range(word_count)]
    chinese_word = set()
    for _ in range(chinese_count):
        chinese_word.add(random.choice(s))
    return len(chinese_word)


print(chinese())
print(simulate(650, chinese()[1]))