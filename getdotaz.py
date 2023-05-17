import sqlite3

connection = sqlite3.connect('p_kompas.db')
cursor = connection.cursor()


cursor.execute(''' CREATE TABLE IF NOT EXISTS otazky(id_otazky integer, otazka text, smer_posunu char, hodnota integer)''')
data_list = [
(1,"Mělo by být možné volit po internetu?","Y",-1),
(2,"Mělo by Česko příjmout Euro?", "Y",-1),
(3,"Měla by minimální mzda do roku 2025 dosáhnout 20 000 Kč?", "X",-2),
(4,"Stát by měl do hospodářství zasahovat co nejméně", "X",2)
]

cursor.executemany("INSERT INTO otazky values (?,?,?,?)", data_list) 

for row in cursor.execute("select * from otazky"):
    print(row)

print(data_list[0][1])
connection.close()