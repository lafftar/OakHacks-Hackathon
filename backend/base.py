import twitter
import yfinance
from backend.db_interface import create_connection
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta
from json import dumps
import matplotlib.pyplot as plt
from seaborn import lineplot


def get_tweet_history(username):
    api_key = "l6W2qcWFlQIvj7wVbkQu4t9qo"
    api_key_secret = "NCu9kQIM8E0n16e1NBXVSFBbeq0ovcG9pQuo2oerNDNXg327To"
    access_token = "757375703809724416-Bjs7FAyO9e7qeUW7zVTWlU3e9ALuZPd"
    access_token_secret = "VlUNDQp5NvdidG1CSuy74mxiQAeQoJ2GqILf1Xsu4sPWU"

    api = twitter.Api(consumer_key=api_key,
                      consumer_secret=api_key_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

    tweets = api.GetUserTimeline(screen_name=username)
    tweet_dict = {
        "Created At": [],
        "Tweet Text": []
    }
    for tweet in tweets:
        created_at = tweet.created_at
        created_at = datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
        created_at = created_at - timedelta(hours=4)  # - 4 hrs for EST time
        created_at = datetime.strftime(created_at, "%Y-%m-%d %H:%M:00-04:00")
        tweet_dict["Created At"].append(created_at)
        tweet_dict["Tweet Text"].append(tweet.text)
    return tweet_dict


def write_tweets_to_db(username, tweet_dict):
    db_connection = create_engine('sqlite:///base.db')
    data_frame = pd.DataFrame(tweet_dict)
    data_frame.to_sql(f"{username}_tweets", if_exists='replace', method='multi',
                      con=db_connection, chunksize=100, index=False)


def get_stock_data(ticker):
    stock = yfinance.Ticker('tsla')
    # stock history for the past day
    data_frame = pd.DataFrame(stock.history(period="1d", actions=False, interval="1m"))
    print(data_frame)
    return data_frame

# 2020-09-11 15:56:00-04:00
# print(dumps(get_tweet_history("elonmusk"), indent=2))
msft = get_stock_data('msft')
# print(msft['Close'])
# msft['Close'].plot()
# plt.show()
# create_connection()

# # data_frame.to_sql(f"elonmusk_fin_data", if_exists='replace', method='multi', con=db_connection, chunksize=100, index=False)
# data_frame = pd.read_sql_table('elonmusk_fin_data', con=db_connection)
# print(data_frame)
