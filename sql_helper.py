select_all = """SELECT * FROM popular_movies;"""

select_one = """SELECT index, rank, title, year FROM popular_movies 
        WHERE rank = '3';"""

insert_one = """INSERT INTO popular_movies(index, rank, title, year) VALUES(
    '100', '101', 'XXXX', 'XXXX');"""

#customers and orders are lists of tuples with the info for each ?
add_many = cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", customers)
add_many2 = cur.executemany("INSERT INTO orders VALUES(?, ?, ?, ?);", orders)