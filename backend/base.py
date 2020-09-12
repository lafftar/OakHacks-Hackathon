import twitter
import yfinance
from backend.db_interface import create_connection
from sqlalchemy import create_engine
import pandas as pd
from pytz import timezone
from datetime import datetime

API_KEY = "l6W2qcWFlQIvj7wVbkQu4t9qo"
API_KEY_SECRET = "NCu9kQIM8E0n16e1NBXVSFBbeq0ovcG9pQuo2oerNDNXg327To"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAANyKHgEAAAAAI2s%2BZF210U4" \
               "mJ1T9t4vso%2F31QBU%3D8Z03aO24yZ43Qw0Fl1TLiQMt34ZlrrCHyIfuc" \
               "YKD8o0DgpVUux"
ACCESS_TOKEN = "757375703809724416-Bjs7FAyO9e7qeUW7zVTWlU3e9ALuZPd"
ACCESS_TOKEN_SECRET = "VlUNDQp5NvdidG1CSuy74mxiQAeQoJ2GqILf1Xsu4sPWU"

api = twitter.Api(consumer_key=API_KEY,
                  consumer_secret=API_KEY_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


items = api.GetUserTimeline(screen_name="elonmusk")
print(items[3])
eastern = timezone('US/Eastern')
utc = timezone('UTC')

created_at = datetime.strptime(items[0].created_at, '%a %b %d %H:%M:%S +0000 %Y')
utc_created_at = utc.localize(created_at)
print(created_at)
print(utc_created_at)

# db_connection = create_engine('sqlite:///base.db')
#
# tweet_dict = {
#     "Created At": [],
#     "Tweet Text": []
# }
# for item in items:
#     tweet_dict["Created At"].append(item.created_at)
#     tweet_dict["Tweet Text"].append(item.text)
#
# print(tweet_dict)
# data_frame = pd.DataFrame(tweet_dict)
# print(data_frame)
# data_frame.to_sql(f"elonmusk_tweets", if_exists='replace', method='multi', con=db_connection, chunksize=100, index=False)
# create_connection()
# stock = yfinance.Ticker('tsla')
# # data_frame = pd.DataFrame(stock.history(period="1d", actions=False, interval="1m"))
# # data_frame.to_sql(f"elonmusk_fin_data", if_exists='replace', method='multi', con=db_connection, chunksize=100, index=False)
# data_frame = pd.read_sql_table('elonmusk_fin_data', con=db_connection)
# print(data_frame)
