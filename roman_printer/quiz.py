import sqlite3
import random

conn = sqlite3.connect("roman.db")
cur = conn.cursor()

cur.execute("SELECT japanese, romaji FROM words")
rows = cur.fetchall()

question = random.choice(rows)

print("【問題】")
print(question[0])
input("Enterキーを押すと答えが出ます")

print("【答え】")
print(question[1])

conn.close()
