from pymecab.pymecab import PyMecab
from readTweets import Read_Tweets


class Mecab:

    def write_tokens(self, tokens_list):
        with open('mecab_tweets.txt', 'w') as f:
            for tokens in tokens_list:
                text = [token.surface for token in tokens]
                text = ' '.join(text)
                f.write(text)
                f.write('\n')


    def do_mecab(self, tweets):
        mecab = PyMecab()
        tokens_list = [mecab.tokenize(tweet) for tweet in tweets]
        self.write_tokens(tokens_list)


def main():
    reader = Read_Tweets()
    tweets = reader.read_tweets('./tweets.csv')
    mecab = Mecab()
    mecab.do_mecab(tweets)


if __name__ == '__main__':
    main()
