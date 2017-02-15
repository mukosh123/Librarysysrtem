import sqlite3 as lite


books = (
('The Grass is Always Greener','Modern Times'),
('Murder!','Crime'),
('Occurrence','Adventure'),
('A Boy at Seven','First Edition'),
('The Higgler','Romance')
)
con = lite.connect('books.db')

with con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS reps")
    cur.execute("CREATE TABLE reps(rep_title TEXT,category TEXT )")
    cur.executemany("INSERT into reps VALUES(?, ?)", books)
