from mysql.connector import connect, Error
from sql_scripts import *
from getpass import getpass


class Reviewer:
    def __init__(self, data: tuple):
        self.last,  self.first = data

    # def __str__(self):
    #     return f'last: {self.first}, first: {self.last}'


reviewers = []

try:
    with connect(
        host='localhost',
        user='root',
        password='26091998@Asd',
        database='p22'
    ) as conn:
        # print(conn)

        with conn.cursor() as cur:
            # cur.execute('use p22;')
            # cur.execute(CREATE_TABLE_RATING)
            # cur.execute(SHOW_TABLE_QUERY.format('rating'))
            # [print(db)for db in cur.fetchall()]
            #
            # alter_table_query = 'alter table `rating` modify ' \
            # 'column `rating` decimal(3, 1) check(`rating` <= 10.0 and `rating` >= 0.0);'
            # cur.execute(alter_table_query)
            # cur.execute(SHOW_TABLE_QUERY.format('rating'))
            # [print(db) for db in cur.fetchall()]
            # cur.execute(INSERT_INTO_MOVIE.format('Film5', 1999, 'Horror'))
            # conn.commit()
            # ls = [(1, 1, 7.2), (2, 2, 5.2), (5, 3, 8.8)]
            # with conn.cursor() as curr:
            #     curr.executemany(INSERT_INTO_RATING, ls)
            #     conn.commit()
            # cur.execute(SELECT_FROM_BY_LIMIT.format(', '.join(
            #     [
            #         '`first_name`',
            #         '`last_name`'
            #     ]),
            #     'reviewer',
            #     5
            # ))
            # [reviewers.append(Reviewer(row)) for row in cur.fetchall()]
            # cur.execute(SELECT_FROM_AND_MAX_AND_MIN.format(', '.join(
            #     [
            #         '`id`'
            #     ]),
            #     ', '.join(
            #         [
            #             '`id`'
            #         ]),
            #     'movie'
            # ))
            cur.execute(SELECT_FROM_TOP_BY_LIMIT)
            for row in cur.fetchall():
                print(row)
    # [print(i.first,i.last) for i in reviewers]


except Error as e:
    print(e)

