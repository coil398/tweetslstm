from load_data import load_data
import tensorflow
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Activation
from tensorflow.python.keras.layers import LSTM
from tensorflow.python.keras.optimizers import RMSprop
from tensorflow.python.keras import backend as K
# from tensorflow.python.keras.utils.visualize_util import plot
# from tensorflow.python.keras.utils import plot_model
import numpy as np
import sys


config = tensorflow.ConfigProto()
config.gpu_options.allow_growth = True
sess = tensorflow.Session(config=config)
K.set_session(sess)


tweet_list, strings, index = load_data()


model = Sequential()
model.add(LSTM(32, input_shape=(len(strings), len(strings))))
model.add(Dense(len(strings)))
model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

# plot_model(model, to_file='LSTM_model.png')

def create_zero_vectors(tweet, strings):
    X = np.zeros((len(tweet), len(strings), len(strings)), dtype=np.bool)
    y = np.zeros((len(tweet), len(strings)), dtype=np.bool)
    return X, y

def vectorize(tweet, strings, index):
    X, y = create_zero_vectors(tweet, strings)
    for i in range(0, len(tweet)-2):
        X[i, index[tweet[i]], index[tweet[i+1]]] = 1
        y[i, index[tweet[i+2]]] = 1
    return X, y

def create_data(tweet, strings, index):
    X, y = vectorize(tweet, strings, index)
    return X, y

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

for i in range(0, 100):
    print()
    print('-' * 50)
    print('Iteration: ' + str(i))
    for tweet in tweet_list:
        X, y = create_data(tweet, strings, index)
        model.fit(X, y, batch_size=32, epochs=10)

    model.save('keras_LSTM.h5')

    for diversity in [0.2, 0.5, 1.0, 1.2]:
        generated_text = list()
        random = random.randint(0, len(tweet_list) - 1)
        start_word = tweet_list[random][0]
        second_word = tweet_list[random][1]
        words = [start_word, second_word]
        generated_text.extend(words)
        print('start words: ' + str(words))

        for i in range(10):
            x = np.zeros((1, 1, len(strings)))
            x[0, index[words[0]], index[words[1]]] = 1
            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_string = index.keys()[index.values().index(next_index)]
            words = [words[1], next_string]
            generated_text.append(next_string)

            sys.stdout.write(generated_text)
            sys.stdout.flush()
        print()
