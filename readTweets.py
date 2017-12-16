import os
import pandas as pd


class Read_Tweets:

    def extract_tweets_data(self, csv_data):
        tweets_data = csv_data['text']
        return tweets_data

    def read_csv_file(self, path):
        csv_data = pd.read_csv(path)
        return csv_data

    def read_tweets(self, path: str):
        csv_data = self.read_csv_file(path)
        tweets_data = self.extract_tweets_data(csv_data)
        tweets = [tweet for tweet in tweets_data]
        return tweets

def main():
    CSV_FILE_PATH = './tweets.csv'
    Reader = Read_Tweets()
    tweets = Reader.read_tweets(CSV_FILE_PATH)
    print(tweets)
    print('length of tweets: ' + str(len(tweets)))


if __name__ == '__main__':
    main()
