# import sqlite3

# conn = sqlite3.connect('datas.db')
# cur = conn.cursor()

# cur.execute('CREATE TABLE IF NOT EXISTS Items (id INTEGER PRIMARY KEY AUTOINCREMENT,party_name TEXT NOT NULL,bill_no TEXT NOT NULL,barcode TEXT NOT NULL,item_name TEXT NOT NULL,    article_no TEXT NOT NULL,size TEXT,purchase_price REAL NOT NULL,sale_price REAL NOT NULL,quantity INTEGER NOT NULL);')

# conn.commit()

# insert_query = """
# SELECT * FROM Items;
# """
# data = cur.execute(insert_query)
# print(data)
# for i in data:
#     print(i)

data = [
    (1, 'ABC Traders', '12345', '9876543210', 'Shirt', '1001', 'M', 500.0, 800.0, 50),
    (2, 'XYZ Supplies', '67890', '1234567890', 'Trousers', '1002', 'L', 700.0, 1100.0, 30),
    (3, 'PQR Wholesale', '11111', '4561237890', 'Jacket', '2003', 'XL', 1200.0, 1800.0, 15),
    (4, 'LMN Retail', '22222', '7894561230', 'Jeans', '3004', 'S', 600.0, 900.0, 40),
    (5, 'DEF Corporation', '33333', '3216549870', 'Cap', '4005', 'Free', 200.0, 350.0, 100),
    (6, 'GHI Imports', '44444', '6547891230', 'Shoes', '5006', '42', 1500.0, 2500.0, 20),
    (7, 'JKL Distributors', '55555', '9873216540', 'T-shirt', '6007', 'M', 400.0, 600.0, 75),
    (8, 'MNO Supplies', '66666', '1237894560', 'Sweater', '7008', 'L', 1000.0, 1500.0, 25),
    (9, 'RST Exporters', '77777', '7891234560', 'Scarf', '8009', 'One Size', 300.0, 500.0, 60),
    (10, 'UVW Traders', '88888', '3219876540', 'Hat', '9010', 'Adjustable', 250.0, 450.0, 80)
]
list = []
# id, party_name, bill_no, barcode, item_name, article_no, size, purchase_price, sale_price, quantity = map()
# feilds = [id, party_name, bill_no, barcode, item_name, article_no, size, purchase_price, sale_price, quantity]

for i in data:
    for j in i:
        list.append(j)

print(list)

