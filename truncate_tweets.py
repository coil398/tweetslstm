import re


class TruncateTweets:

    __tweet_list = list()
    __url_pattern = re.compile(r'https?://')

    def __init__(self, tweet_list):
        self.__tweet_list = tweet_list

    def delete_bot_tweets(self, string_list):
        if string_list[0][0] == '午':
            self.__tweet_list.remove(' '.join(string_list))

    def delete_retweets(self, string_list):
        if string_list[0] == 'RT':
            try:
                self.__tweet_list.remove(' '.join(string_list))
            except ValueError:
                # print(string_list)
                pass

    def delete_reply_names(self, string_list):
        for string in string_list:
            try:
                if string[0] == '@':
                    try:
                        self.__tweet_list.remove(' '.join(string_list))
                    except ValueError:
                        pass
            except IndexError:
                pass

    def delete_tweets_having_urls(self, string_list):
        for string in string_list:
            if self.__url_pattern.match(string):
                try:
                    self.__tweet_list.remove(' '.join(string_list))
                except ValueError:
                    # print(string_list)
                    pass

    def truncate(self):
        for tweet in self.__tweet_list[:]:
            string_list = tweet.split(' ')
            self.delete_bot_tweets(string_list)
            self.delete_retweets(string_list)
            self.delete_reply_names(string_list)
            self.delete_tweets_having_urls(string_list)

    def get_truncated_tweets(self):
        self.truncate()
        return self.__tweet_list
