import sqlite3

# データベース作成（なければ自動で作られる）
conn = sqlite3.connect("roman.db")
cur = conn.cursor()

# テーブル作成
cur.execute("""
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    japanese TEXT NOT NULL,
    romaji TEXT NOT NULL
)
""")

# 初期データ
data = [
    ("あさ", "asa"),
    ("ひる", "hiru"),
    ("よる", "yoru"),
    ("がっこう", "gakkou"),
    ("せんせい", "sensei")
]

cur.executemany(
    "INSERT INTO words (japanese, romaji) VALUES (?, ?)",
    data
)

conn.commit()
conn.close()

print("データベースを作成しました")
