import sqlite3

# connect db file under current direction
connection = sqlite3.connect('data.sqlite3')

cursor = connection.cursor()

create_table = "CREATE TABLE users(id int, username text, password text)"

cursor.execute(create_table)

user = (1, 'ben', 'pwd')
insert_query = "INSERT into users Values (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (1, 'ben', 'pwd'),
    (1, 'ben', 'pwd')
]
cursor.executemany(insert_query, users)

connection.commit()
connection.close()
