import csv

with open("kanji.csv", encoding="cp932") as f:
  reader = csv.reader(f)
  data = list(reader)[1:]

# f = open("kanji.csv", encoding="cp932")
# reader = csv.reader(f)
# data =list(reader)
# f.close()

import random

# stats["total"] = 0
# accuracy_rate = 0
# stats["correct"] = 0
# wrong_answers = 0

# accuracy_rate = 0

stats = {"total":0,"correct":0, "wrong": 0}

def quiz(data, stats):
  # global stats["total"], accuracy_rate, stats["correct"], wrong_answers
  while True:
    question, answer = random.choice(data)
    print(f"問題:{question}")

    kotae=input("答えは？(0でおわり)").strip()
    
    match kotae:
      case "0":
        print(f'今回の問題数は{stats["total"]}、正解数は{stats["correct"]}個、不正解数は{stats["wrong"]}、正答率は{accuracy_rate:.1f}％でした')
        match accuracy_rate:
          case _ if accuracy_rate >= 90:
            print("Excellent!!")
          case _ if accuracy_rate >= 70:
            print("Good job!")
          case _:
            print("Keep going!")
        break
      case _ if kotae == answer:
        print("good!!")
        stats["correct"] += 1
      case _:
        print("No 解答は:", answer)
        stats["wrong"] += 1
    stats["total"] += 1
    accuracy_rate = stats["correct"] / stats["total"] * 100
    print(f'今の問題数は{stats["total"]}、正解数は{stats["correct"]}個、不正解数は{stats["wrong"]}、正答率は{accuracy_rate:.1f}％です')

quiz(data,stats)

  # print(f"問題:{question}")
  # kotae=input("答えは？(0でおわり)").strip()
  # if kotae == answer:
  #   print("good!!")
  #   
  #stats["correct"]
  # += 1
  # else:
  #   print("No 解答は:", answer)
  # else:


# print(data)