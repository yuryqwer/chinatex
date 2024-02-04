import os
import unicodedata
from pprint import pprint


def chinese():
    chinese_count = 0
    chinese_word = {}

    for filename in os.listdir("./real_captcha"):
        color, text, *_ = filename[:-4].split("_")
        for c in text:
            if 'CJK' in unicodedata.name(c):
                chinese_count += 1
                chinese_word.setdefault(c, 0)
                chinese_word[c] += 1

    return len(chinese_word), chinese_count, chinese_word


length, count, word = chinese()
print("目前一共出现的汉字数量：", length)

with open("./font/chinese7000.txt", encoding="utf-8") as f:
    word_list = [i for i in f.readline()]

print("索引", "出现次数")
pprint(sorted((word_list.index(w), word[w]) for w in word))