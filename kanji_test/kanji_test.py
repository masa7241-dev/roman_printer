import csv
f = open("kanji.csv", encoding="cp932")
reader = csv.reader(f)
data =list(reader)
f.close

import random

aa = 0
bb = 0
cc = 0
dd = 0
while True:
  question, answer = random.choice(data)
  print(f"問題:{question}")
  kotae=input("答えは？(0でおわり)").strip()
  match kotae:
    case "0":
      print(f"今回の問題数は{aa}、正解数は{cc}個、不正解数は{dd}、正答率は{bb:.1f}％でした")
      break
    case _ if kotae == answer:
      print("good!!")
      cc += 1
    case _:
      print("No 解答は:", answer)
      dd += 1
  aa += 1
  bb = cc / aa * 100
  print(f"今の問題数は{aa}、正解数は{cc}個、不正解数は{dd}、正答率は{bb:.1f}％です")
    
  # print(f"問題:{question}")
  # kotae=input("答えは？(0でおわり)").strip()
  # if kotae == answer:
  #   print("good!!")
  #   cc += 1
  # else:
  #   print("No 解答は:", answer)
  # else:


# print(data)