import sqlite3

conn = sqlite3.connect('shallownowschool.db')

cursor = conn.cursor()

cursor.execute("""
    SELECT *
    FROM tb_estudante;
""")

for linha in cursor.fetchall():
    print('Bonjour,', linha[1], '!')

conn.close()
