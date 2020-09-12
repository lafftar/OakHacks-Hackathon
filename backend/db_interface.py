import sqlite3


def create_connection():
    # this method of connecting might cause a problem later, I tried getcwd but that didnt
    # work, I tried exact path, but that will cause problems with different systems.
    conn = sqlite3.connect(r'base.db', isolation_level=None)
    return conn


def create_table(table_name):
    create_table_sql = f"""CREATE TABLE {table_name}(
                            page_number integer PRIMARY KEY, 
                            api_data text,
                            date_time text
                        );"""
    cursor().execute(create_table_sql)