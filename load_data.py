import numpy as np
from itertools import chain


MAXLEN = 10


def load_text():
    with open('./mecab_tweets.txt', 'r') as f:
        text = f.read()
    return text

def create_tweet_list(text):
    tweets = text.split('\n')
    tweets_list = [tweet.split(' ') for tweet in tweets]
    return tweets_list

def truncate_tweets(tweet_list):
    truncater = TruncateTweets(tweet_list)
    truncated_tweets = truncater.get_truncated_tweets()
    return truncated_tweets

def create_strings_data(tweet_list):
    temp_list = list(chain.from_iterable(tweet_list))
    strings_set = set(temp_list)
    strings = sorted(list(strings_set))
    return strings

def create_index(strings):
    index = {c: i for (i, c) in enumerate(strings)}
    return index

def get_maxlen(tweets):
    maxlen = 0
    for tweet in tweets:
        if len(tweet) > maxlen:
            maxlen = len(tweet)
    return maxlen

def create_zero_vectors(tweet_list, strings):
    X = np.zeros((10, len(strings), len(strings)), dtype=np.bool)
    y = np.zeros((10, len(strings)), dtype=np.bool)
    return X, y

def vectorize(tweet_list, strings, index):
    X, y = create_zero_vectors(tweet_list, strings)
    i = 0
    for tweet in tweet_list:
        for i in range(0, len(tweet)-2):
            X[i, index[tweet[i]], index[tweet[i+1]]] = 1
            y[i, index[tweet[i+1]]] = 1
            i += 1
            if i == 10000*10:
                break
    return X, y

# def vectorize(tweet_list, maxlen, strings, index):
#     X, y = create_zero_vectors(tweet_list, maxlen, strings)
#     for i, tweet in enumerate(tweet_list):
#         for t, string in enumerate(tweet):
#             if t == 0:
#                 y[i, index[string]] = 1
#             else:
#                 X[i, t, index[string]] = 1
#     return X, y

# def load_data():
#     text = load_text()
#     tweet_list = create_tweet_list(text)
#     # tweet_list = truncate_tweets(tweet_list)
#     strings = create_strings_data(tweet_list)
#     index = create_index(strings)
#     maxlen = get_maxlen(tweet_list)
#     return tweet_list, strings, index, maxlen

def load_data():
    text = load_text()
    tweet_list = create_tweet_list(text)
    # tweet_list1 = tweet_list[:10000]
    # tweet_list2 = tweet_list[10000: 20000]
    # tweet_list3 = tweet_list[20000:]
    # tweet_list = truncate_tweets(tweet_list)
    strings = create_strings_data(tweet_list)
    index = create_index(strings)
    return tweet_list, strings, index
    # maxlen = get_maxlen(tweet_list)
    # print(vectorize(tweet_list, strings, index))
    # X1, y1 = vectorize(tweet_list1, strings, index)
    # X2, y2 = vectorize(tweet_list2, strings, index)
    # X3, y3 = vectorize(tweet_list3, strings, index)
    # X, y = vectorize(tweet_list, strings, index)
    # return strings, index, X, y


if __name__ == '__main__':
    load_data()
