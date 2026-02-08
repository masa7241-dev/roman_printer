import csv
import random

# Selecta subject
print("Which subuject do you learn ?")
print('1:kanji  2:english  3:electric 4:wrong_kanji 5:wrong_english')
file_number = input("Select subject")

match file_number:
  case "1":
    filename = "kanji.csv"
  case "2":
    filename = "english.csv"
  case "3":
    filename = "electric.csv"
  # case "4":
  #   filename = "review_kanji.csv"
  # case "5":
  #   filename = "review_english.csv"
  case _:
    print("That number cannot be selected.")
    exit()

# Import a csv file
with open(filename, encoding="cp932") as f:
  reader = csv.reader(f)
  data = list(reader)[1:]


# quiz function
def quiz(data):
  wrong_dict={}
  stats = {"total":0,"correct":0, "wrong": 0}
  while True:
    question, answer = random.choice(data)
    print(f"問題:{question}")

    kotae=input("答えは？(0でおわり)").strip()
    
    match kotae:
      case "0":
        show_final_result(stats,wrong_dict)
        accuracy_rate = calc_accuracy(stats)
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

        if question in wrong_dict:
          wrong_dict[question]["count"] += 1
        else:
          wrong_dict[question] = {"answer": answer, "count": 1}

    stats["total"] += 1
    
    show_result(stats)
  
  return stats,wrong_dict

# calculate accuracy
def calc_accuracy(stats):
  if stats["total"] == 0:
    return 0
  return stats["correct"] / stats["total"] * 100

# display results
def show_result(stats):
  accuracy_rate = calc_accuracy(stats)
  print(f'今の問題数は{stats["total"]}、正解数は{stats["correct"]}個、不正解数は{stats["wrong"]}、正答率は{accuracy_rate:.1f}％です')
  
# display final results
def show_final_result(stats,wrong_dict):
  accuracy_rate = calc_accuracy(stats)
  print(f'今回の問題数は{stats["total"]}、正解数は{stats["correct"]}個、正答率は{accuracy_rate:.1f}％です')
  print("今回間違えた問題は")
  for q,v in wrong_dict.items():
    print(f"{q}{v['count']}回")

def save_wrong_dict(wrong_dict,filename):
  if not wrong_dict:
    return
  else:
    review_filename = f"review_{filename}"
    with open(review_filename, "w", encoding="cp932", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(["question","answer","count"])
      for q, v in wrong_dict.items():
        writer.writerow([q,v["answer"],v["count"]])
    return review_filename
            

stats,wrong_dict=quiz(data)
save_wrong_dict(wrong_dict,filename)
print("Would you like to practice the questions you got wrong again?")
select_Challenge = input("y/n")
if select_Challenge == "y":
  review_data = [(q, v["answer"]) for q, v in wrong_dict.items()]
  quiz(review_data)
else:
  exit()

