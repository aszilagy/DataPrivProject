from simpleRSA import *
import random
import sys
import os
import pickle

def main():
    createKey()

def createKey():
    public_key, private_key = make_key_pair(32)  # safe for n<100

    if os.path.isfile('Keys.pkl'):
        with open('Keys.pkl', 'rb') as fb:
            keys = pickle.load(fb)

    else:
        keys = {'KEY_DICT': (public_key, private_key)}
        with open('Keys.pkl', 'wb') as fw:
            pickle.dump(keys, fw)


    print(keys)

if __name__ == '__main__':
    main()

