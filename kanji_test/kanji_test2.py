import csv
import random

with open("kanji.csv", encoding="cp932") as f:
  reader = csv.reader(f)
  data = list(reader)[1:]

stats = {"total":0,"correct":0, "wrong": 0}
wrong_list=[]

def quiz(data, stats):
  while True:
    question, answer = random.choice(data)
    print(f"問題:{question}")

    kotae=input("答えは？(0でおわり)").strip()
    
    match kotae:
      case "0":
        show_final_result(stats)
        accuracy_rate = calc_accuracy(stats)
        match accuracy_rate:
          case _ if accuracy_rate >= 90:
            print("Excellent!!")
          case _ if accuracy_rate >= 70:
            print("Good job!")
          case _:
            print("Keep going!")
            print(f"今回間違えた問題は{wrong_list}")
        break

      case _ if kotae == answer:
        print("good!!")
        stats["correct"] += 1

      case _:
        print("No 解答は:", answer)
        stats["wrong"] += 1
        wrong_list.append((question, answer))

    stats["total"] += 1
    
    show_result(stats)

def calc_accuracy(stats):
  if stats["total"] == 0:
    return 0
  return stats["correct"] / stats["total"] * 100

def show_result(stats):
  accuracy_rate = calc_accuracy(stats)
  print(f'今の問題数は{stats["total"]}、正解数は{stats["correct"]}個、不正解数は{stats["wrong"]}、正答率は{accuracy_rate:.1f}％です')
  
def show_final_result(stats):
  accuracy_rate = calc_accuracy(stats)
  print(f'今回の問題数は{stats["total"]}、正解数は{stats["correct"]}個、正答率は{accuracy_rate:.1f}％です')

quiz(data,stats)

