import sqlite3

# connect db file under current direction
connection = sqlite3.connect('data.sqlite3')

cursor = connection.cursor()

# Create table
create_table = "CREATE TABLE users(id int, username text, password text)"

cursor.execute(create_table)

# Insert data
user = (1, 'ben1', 'pwd')
insert_query = "INSERT into users Values (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, 'ben2', 'pwd'),
    (3, 'ben3', 'pwd')
]
cursor.executemany(insert_query, users)

# Select
select_query = "select id from users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
