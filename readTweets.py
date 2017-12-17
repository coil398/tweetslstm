import os
import pandas as pd
from truncate_tweets import TruncateTweets


class Read_Tweets:

    def extract_tweets_data(self, csv_data):
        tweets_data = csv_data['text']
        return tweets_data

    def read_csv_file(self, path):
        csv_data = pd.read_csv(path)
        return csv_data

    # def delete_reply_names(self, tweet):
    #     print(tweet)
    #     if tweet[0] == '@':
    #         tweet_list = tweet.split(' ')
    #         tweet_list = tweet_list[1:]
    #         tweet = ' '.join(tweet_list)
    #     return tweet

    def read_tweets(self, path: str):
        csv_data = self.read_csv_file(path)
        tweets_data = self.extract_tweets_data(csv_data)
        tweets = [tweet for tweet in tweets_data]
        truncater = TruncateTweets(tweets)
        truncated_tweets = truncater.get_truncated_tweets()
        # print(truncated_tweets)
        return tweets

def main():
    CSV_FILE_PATH = './tweets.csv'
    reader = Read_Tweets()
    tweets = reader.read_tweets(CSV_FILE_PATH)
    print(tweets)
    print('length of tweets: ' + str(len(tweets)))


if __name__ == '__main__':
    main()
