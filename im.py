# Toshmurodov Yusufjon N42
'''
import psycopg2
from psycopg2._psycopg import cursor

host = 'localhost'
user = 'postgres'
password = '123'
database = 'n47'
port = 5432

connect = psycopg2.connect("dbname='n42' "
                           "user='postgres' "
                           "host='localhost' "
                           "password='<123>'"
                           "port='5432' "
                           )
db = connect.cursor()
cur = connect.cursor()

create_product_table = """
CREATE TABLE IF NOT EXISTS products1 (
                                        id integer PRIMARY KEY,
                                        name varchar(100) NOT NULL,
                                        price integer NOT NULL,
                                        color varchar(100) NOT NULL,
                                        image varchar(255) NOT NULL,
 );"""


def insert_products1(name, price, color, image):
    name = str(input('Enter products1 name: '))
    price = str(input('Enter products1 price : '))
    color = str(input('Enter products1 color : '))
    image = str(input('Enter products1 image : '))
    insert_into_query = "insert into books(name,price,color,image) values (%s,%s,%s,%s);"
    insert_into_params = (name,price,color,image)
    cur.execute(insert_into_query, insert_into_params)



def select_all_products1():
    select_query = 'select * from products1;'
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
         print_response(str(row))


def update_products1(name, price, color, image):
    select_all_products1()
    _id = int(input('Enter product id: '))
    name = str(input('Enter new products name : '))
    price = str(input('Enter new price : '))
    color = str(input('Enter new color : '))
    image = str(input('Enter new image : '))
    update_query = 'update products set name = %s, price = %s,color = %s, image =%s where id =%s;'
    update_query_params = (name, price,color,image,_id)
    cur.execute(update_query, update_query_params)
    cur.execute(create_product_table)
    print_response('Successfully updated products1')


def delete_products1(id):
    select_all_products1()
    _id = int(input('Enter products1 id : '))

    delete_query = 'delete from products where id = %s;'
    cur.execute(delete_query, (_id,))
    conn.commit()
    print_response('Successfully deleted products1')




'''





# 3-masala
def my_generator():
    yield 1
    yield 2
    yield 3


arr1 = ['a', 'b', 'c', 'd', 'e']
arr2 = [1, 2, 3, 4, 5]

my_gen = {key: value for key, value in zip(arr1, arr2)}
print(my_gen)


'''
# 4- masala
class Alphabet :
    for i in ('a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','s','t','u','v','w','x','y','z'):
        print(i)
'''









