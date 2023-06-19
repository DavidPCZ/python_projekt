import sqlite3


def getdotazf(id_otazky, data):
    connection = sqlite3.connect('p_kompas.db')
    cursor = connection.cursor()

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS otazky(id_otazky integer, otazka text, smer_posunu char, hodnota integer)''')

    data_list = [
        (1, "Mělo by být možné volit po internetu?", "Y", -1),
        (2, "Měla by minimální mzda do roku 2025 dosáhnout 20 000 Kč?", "X", -1),
        (3, "Mělo by Česko příjmout Euro?", "Y", -1),
        (4, "Stát by měl do hospodářství zasahovat co nejméně", "X", 1),
        (5, "Občané by měli mít právo rozhodovat v referendech i o důležitých otázkách", "Y", 1),
        (6, "Souhlasím s vyšším zdaněním fyzických osob, které vydělávají více než trojnásobek průměrné mzdy", "X", -1),
        (7, "Měly by být znovu zavedeny poplatky u lékaře a za pobyt v nemocnici?", "X", 1),
        (8, "Měli by studenti na veřejných vysokých školách platit školné?", "X", 1),
        (9, "Měla by se zrušit inkluze ve školách?", "Y", 1),
        (10, "Mělo by být vlastnictví zbraně zakotveno v Listině základních práv a svobod?", "X", 1),
        (11, "Měla by česká vláda podporovat Evropskou komisi a Evropský parlament v kritice Polska a Maďarska?", "Y", -1),
        (12, "Podporujete tzv. Green deal?", "Y", -1),
        (13, "Lidé by měli mít možnost připlatit si za nadstandart ve zdravotnictví", "X", 1),
        (14, "Vzhledem k neúměrně vysokým cenám bydlení ve větším městech by se měla zavést částečná regulace pro investory do nemovitostí", "X", 1)
        (15, "-------------", "X", 1)
    ]
    global pocet_otazek
    pocet_otazek = len(data_list)

    cursor.executemany("INSERT INTO otazky VALUES (?,?,?,?)", data_list)

    sql_dotaz = "SELECT otazka FROM otazky WHERE id_otazky = ?"
    cursor.execute(sql_dotaz, (id_otazky,))
    sql_dotaz = cursor.fetchone()
    sql_dotaz = sql_dotaz[0]

    smer = "SELECT smer_posunu FROM otazky WHERE id_otazky = ?"
    cursor.execute(smer, (id_otazky,))
    smer = cursor.fetchone()
    smer = smer[0]

    hodnota = "SELECT hodnota FROM otazky WHERE id_otazky = ?"
    cursor.execute(hodnota, (id_otazky,))
    hodnota = cursor.fetchone()
    hodnota = hodnota[0]

    # print(data)

    if data == 1:
        print("sql dotaz: ", sql_dotaz)
        result = sql_dotaz
    elif data == 2:
        print("směr: ", smer)
        result = smer
    elif data == 3:
        print("hodnota: ", hodnota)
        result = hodnota
    return result

    connection.close()


# Volání funkce getdotazf() s parametry
vysledek1 = getdotazf(1, 1)
# print(vysledek1)

vysledek2 = getdotazf(2, 2)
# print(vysledek2)

vysledek3 = getdotazf(3, 3)
# print(vysledek3)
