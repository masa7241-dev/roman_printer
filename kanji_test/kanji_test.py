import csv
f = open("kanji.csv", encoding="cp932")
reader = csv.reader(f)
data =list(reader)
f.close

import random

total_questions = 0
accuracy_rate = 0
correct_answers = 0
wrong_answers = 0
while True:
  question, answer = random.choice(data)
  print(f"問題:{question}")
  kotae=input("答えは？(0でおわり)").strip()
  match kotae:
    case "0":
      print(f"今回の問題数は{total_questions}、正解数は{
      correct_answers
    }個、不正解数は{wrong_answers}、正答率は{accuracy_rate:.1f}％でした")
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
      correct_answers += 1
    case _:
      print("No 解答は:", answer)
      wrong_answers += 1
  total_questions += 1
  accuracy_rate = correct_answers / total_questions * 100
  print(f"今の問題数は{total_questions}、正解数は{correct_answers}個、不正解数は{wrong_answers}、正答率は{accuracy_rate:.1f}％です")

  
  # print(f"問題:{question}")
  # kotae=input("答えは？(0でおわり)").strip()
  # if kotae == answer:
  #   print("good!!")
  #   
  #correct_answers
  # += 1
  # else:
  #   print("No 解答は:", answer)
  # else:


# print(data)