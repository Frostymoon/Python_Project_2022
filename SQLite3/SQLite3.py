import sqlite3


conn = sqlite3.connect('highscores.db')

c = conn.cursor()

# c.execute("""CREATE TABLE highscores(
#             first text,
#             last text,
#             pay integer)""")

# c.execute("INSERT INTO highscores VALUES('Kiri', 'Ac', 170)")

c.execute("SELECT * FROM highscores WHERE last = 'Ac'")

print (c.fetchone())

conn.commit()

conn.close()

