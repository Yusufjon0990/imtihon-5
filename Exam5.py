import psycopg2

from typing import List

# 1.	Postgresql bazaga python yordamida ulaning .
# Product nomli jadval yarating  (id,name,price, color,image) .
db_params = {
    'user': 'postgres',
    'host': 'localhost',
    'database': 'n42',
    'password': '123',
    'port': 5432

}


class DbConnect:
    def __init__(self, db__params: dict):
        self.db_params = db__params
        self.conn = psycopg2.connect(**self.db_params)

    def __enter__(self):
        self.cur = conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur and not self.cur.closed:
            self.conn.commit()
            self.cur.close()
            self.conn.close()


class Products:
    def __init__(self,
                 id: int | None = None,
                 name: str | None = None,
                 price: int | None = None,
                 color: str | None = None,
                 image: str | None = None):
        self.id = id
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def create_table1(self):
        with DbConnect(db_params) as cur1:
            create_table_query = ''' create table if not exists Product(
               id serial primary key,
               name varchar(30) not null,
               price int not null,
               color varchar(30) not null,
               image varchar(100) not null);'''
            cur1.execute(create_table_query)
            print('Successfully created')

    def insert_table(self):
        with DbConnect(db_params) as cur1:
            insert_table_query = ''' insert table Product(name,price,color,image) values(%s,%s,%s,%s)'''
        insertable_params = (self.name, self.price, self.color, self.image)
        cur1.execute(insert_table_query, insertable_params)
        print('INSERT 0 1')


product = Products(name='Phone', price=200, color='black')
product.insert_table()

#2.	Insert_product , select_all_products , update_product,delete_product
#nomli funksiyalar yarating.
def insert_product(name, price, color, image):
    insert_table_query = ''' insert table Product(name,price,color,image) values(%s,%s,%s,%s)'''
    insert_table_params = (name, price, color, image)
    cur.execute(insert_table_query, insert_table_params)
    conn.commit()
    print('INSERT 0 1')


insert_product('Phone', 23232, 'black', 'asasasa')


def select_all():
    select_all_query = '''select * from Product;'''
    cur.execute(select_all_query)
    for i in cur.fetchall():
        print(i)


#
# def delete_pro():
#     delete_table_query = '''delete * from Product where id = %s'''
#     _id: int = int(input('Enter id:  '))
#     cur.execute(delete_table_query, (_id,))
#     print('Successfully deleted')


# delete_pro()


def update_table():
    name = input('Enter name: ')
    id = int(input('Enter id: '))
    update_table_query = ''' update Product set name = %s where id  = %s'''
    update_table_params = (name, id)
    cur.execute(update_table_query, update_table_params)
    conn.commit()


# update_table()


# 3.	Alphabet nomli class yozing .class obyektlarini  iteratsiya qilish imkoni   bo’lsin (iterator)
# obyektni for sikli orqali iteratsiya qilinsa 26 ta alifbo xarflari chiqsin
class Alphabet:
    def __init__(self, letters: List):
        self.index = 0
        self.letters = letters

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.letters):
            raise StopIteration
        else:
            result = self.letters[self.index]
            self.index += 1
            return result


my_words = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X',
            'Y', 'Z', 'SH', 'CH', 'NG']

alphabet = Alphabet(my_words)

# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
# print(next(alphabet))
#
# while True:
#     try:
#         print(next(alphabet))
#     except StopIteration as e:
#         break

#4.	print_numbers va print_leters nomli funksiyalar yarating.
#prit_numbers funksiyasi (1,5) gacha bo’lgan sonlarni , print_letters esa  ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib ,parallel 2ta thread yarating.Ekranga parallel ravishda itemlar chiqsin.

import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(letter)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()
# 5.Product nomli class yarating (1 – misoldagi Product ).Product classiga save() nomli object method yarating.
# Uni vazifasi object attributelari orqali bazaga saqlasin.

db_params: dict = {
    'user': 'postgres',
    'host': 'localhost',
    'database': 'n42',
    'password': '123',
    'port': 5432

}


class DbConnect:
    def __init__(self, db__params: dict):
        self.db_params = db__params
        self.conn = psycopg2.connect(**self.db_params)

    def __enter__(self):
        self.cur = conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur and not self.cur.closed:
            self.conn.commit()
            self.cur.close()
            self.conn.close()


class Products:
    def __init__(self,
                 id: int | None = None,
                 name: str | None = None,
                 price: int | None = None,
                 color: str | None = None,
                 image: str | None = None):
        self.id = id
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def create_table1(self):
        with DbConnect(db_params) as cur1:
            create_table_query = ''' create table if not exists Product(
               id serial primary key,
               name varchar(30) not null,
               price int not null,
               color varchar(30) not null,
               image varchar(100) not null);'''
            cur1.execute(create_table_query)
            print('Successfully created')

    def insert_table(self):
        with DbConnect(db_params) as cur1:
            insert_table_query = ''' insert table Product(name,price,color,image) values(%s,%s,%s,%s)'''
        insertable_params = (self.name, self.price, self.color, self.image)
        cur1.execute(insert_table_query, insertable_params)
        print('INSERT 0 1')


product = Products(name='Samsung', price=350, color='black', image='https://assets.asaxiy.uz/product/items/desktop/c86fff95e6768da783db6dd783f902172023041314111931576jfSc23ZSbQ.jpg.webp')
product.create_table1()
product.insert_table()

#6.	DbConnect nomli ContextManager yarating.
# Va uning vazifasi python orqali PostGresqlga ulanish (conn,cur)
class DbConnect:
    def __init__(self, db__params: dict):
        self.db_params = db__params
        self.conn = psycopg2.connect(**self.db_params)

    def __enter__(self):
        self.cur = conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur and not self.cur.closed:
            self.conn.commit()
            self.cur.close()
            self.conn.close()


class Products:
    def __init__(self,
                 id: int | None = None,
                 name: str | None = None,
                 price: int | None = None,
                 color: str | None = None,
                 image: str | None = None):
        self.id = id
        self.name = name
        self.price = price
        self.color = color
        self.image = image

