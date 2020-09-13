import pandas as pd
from sqlalchemy import create_engine

db_connection = create_engine('sqlite:///../db/base.db')


def get_fin_data(username):
    data_frame = pd.read_sql_table(f'{username}_fin_data', con=db_connection)
    data_frame = data_frame.to_json()
    return data_frame


def get_tweets(username):
    data_frame = pd.read_sql_table(f'{username}_tweets', con=db_connection)
    data_frame = data_frame.to_json()
    return data_frame

# print(get_tweets('elonmusk'))