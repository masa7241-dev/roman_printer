import csv
f = open("kanji.csv", encoding="cp932")
reader = csv.reader(f)
data =list(reader)
f.close

import random

question, answer = random.choice(data)
print(f"問題:{question}")
kotae=input("答えは？")
if kotae == answer:
  print("good!!")
else:
  print("No 解答は:", answer)

# print(data)