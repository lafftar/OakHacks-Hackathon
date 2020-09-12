import sqlite3


def create_connection():
    # this method of connecting might cause a problem later, I tried getcwd but that didnt
    # work, I tried exact path, but that will cause problems with different systems.
    conn = sqlite3.connect(r'base.db', isolation_level=None)
    return conn


def cursor():
    conn = create_connection()
    return conn.cursor()


def create_fin_data_table(table_name):
    create_table_sql = f"""CREATE TABLE {table_name}(
                            date_time date PRIMARY KEY, 
                            open int,
                            high int,
                            low int,
                            close int,
                            volume int
                        );"""
    cursor().execute(create_table_sql)


