import sqlite3
from django.http import request
def item_en():
    conn = sqlite3.connect('datas.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS Items (id INTEGER PRIMARY KEY AUTOINCREMENT,party_name TEXT NOT NULL,bill_no TEXT NOT NULL,barcode TEXT NOT NULL,item_name TEXT NOT NULL,    article_no TEXT NOT NULL,size TEXT,purchase_price REAL NOT NULL,sale_price REAL NOT NULL,quantity INTEGER NOT NULL);')

    conn.commit()

    insert_query = """
    SELECT * FROM Items;
    """
    data = cur.execute(insert_query)
    print(data)
    for i in data:
        print(i)

    Ldata = []
    for i in data:
        for j in i:
            Ldata.append(j)
    
    return Ldata


