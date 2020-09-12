import twitter

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


item = api.GetUserTimeline(screen_name="elonmusk")

for tem in item:
    print(tem)
