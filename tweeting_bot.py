import tweepy
import time
import random

CONSUMER_KEY = 'dBqK896mgOzItAXHzWL4gefUT'
CONSUMER_SECRET = 'hi9pdMAcX88hRBPZ6B0JSONjhh0P7q6DGI0WzVZWsjBOCTH6z8'

ACCESS_KEY = '1228480000078352386-4fFrWqkMrQDtLLyau21t2P0peIPGKv'
ACCESS_SECRET = 'E8N1FXo930WUPNMvxQQCRnGhCqQMUJJgOfz98X3F23EV4'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print("This command works")

words1 = "I feel like I'm Gucci Mane in 2006"
words2 = "I love fornite"
words3 = "follow claarkefn on twitch"
words4 = "New Twitter who dis?"
words5 = "I promise you I'm not a bot"
words6 = "How to make a twitter bot"
words7 = "ya know I could get famous?"
words8 = "Happy Birthday!"
words9 = "How many followers can this totally not a bot account get"
words10 = "It's pretty hard thinking of 10 phrases to randomly tweet everyday"
words11 = "send me tweets, I might respond "


text_files = [words1, words2, words3, words4, words5, words6, words7, words8, words9, words10, words11]

while True:

    api.update_status(text_files[random.randint(1,11)])
    time.sleep(7200)