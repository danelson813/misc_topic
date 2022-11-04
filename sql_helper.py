
insert_one = '''
INSERT INTO
    popular_movies(
        index, rank, title, year
    )
VALUES(
    100, '101', 'XXXX', 'XXX', 
);
'''

select_one = """
SELECT 
    index, rank, title, year
FROM
    popular_movies
WHERE
    rank = '3';
"""

select_all = """
SELECT
    *
FROM
    popular_movies;
"""

#customers and orders are lists of tuples with the info for each ?
insert_many = """
INSERT INTO
    users
VALUES(
    ?,?,?,?
);
""",
customers

