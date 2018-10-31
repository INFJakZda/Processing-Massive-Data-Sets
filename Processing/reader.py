import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_tables(conn):
    sql_create_tracks_table = """ CREATE TABLE IF NOT EXISTS tracks (
                                        track_id varchar(18) NOT NULL,
                                        song_id varchar(18) NOT NULL,
                                        artist varchar(256) DEFAULT NULL,
                                        title varchar(256) DEFAULT NULL,
                                        PRIMARY KEY (track_id)
                                    ); """

    sql_create_sample_table = """ CREATE TABLE IF NOT EXISTS sample (
                                        user_id varchar(18) NOT NULL,
                                        song_id varchar(18) NOT NULL,
                                        date varchar(18) DEFAULT NULL
                                    ); """
    if conn is not None:
        create_table(conn, sql_create_tracks_table)
        create_table(conn, sql_create_sample_table)
    else:
        print("Error! cannot create the database connection.")

def insert_row(values, cursor):
    if len(values) == 3:
        cursor.execute('''INSERT INTO sample VALUES(?,?,?)''', (values[0], values[1], values[2]))
    else:
        cursor.execute('''INSERT INTO tracks VALUES(?,?,?,?)''', (values[0], values[1], values[2], values[3]))

def prepareData(conn):
    cursor = conn.cursor()
    with open("triplets_sample_20p.txt",'r') as fp:
        for line in fp:
            values = line.strip().split('<SEP>')
            insert_row(values, cursor)
    with open("unique_tracks.txt", 'r', encoding = "ISO-8859-1") as fp:
        for line in fp:
            values = line.strip().split('<SEP>')
            insert_row(values, cursor)

def close_connection(conn):
    try:
        conn.close()
    except Error as e:
        print(e)

###############EXERCISES#################
def zad1(cursor):
    cursor.execute("""SELECT title, artist, coun from {
                            SELECT song_id, count(song_id) as coun FROM sample GROUP BY song_id ORDER BY count(song_id) DESC LIMIT 10
                        } JOIN tracks ON song_id""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    print("[INFO] Create database")
    conn = create_connection(":memory:")
    print("[INFO] Connected to database!")

    print("[INFO] Create tables")
    create_tables(conn)
    print("[INFO] Tables created!")


    print("[INFO] Start inserting values to database")
    prepareData(conn)
    print("[INFO] Values inserted")

    cursor = conn.cursor()
    print("[INFO] ZAD 1")
    zad1(cursor)

    print("[INFO] Try to close database")
    close_connection(conn)
    print("[INFO] Database closed! END")
