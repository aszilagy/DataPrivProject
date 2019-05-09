from passlib.hash import sha256_crypt as sha
import argparse
import sys
import paillier as pail
import os
import configparser as cf
import pickle


def main():
    if len(sys.argv) < 3:
        print("Wrong arguments, use format of:   python create_account.py <username> <password>")

    elif len(sys.argv) == 3:
        user = sys.argv[1]
        pa = sys.argv[2]
        print(user, pa)
        createPass(user, pa)

def createPass(user, pa):
    username = sha.encrypt(user)
    password = sha.encrypt(pa)
    priv, pub = pail.generate_keypair(256)

    userD = {}

    if os.path.isfile('UserDB.pkl'):
        with open('UserDB.pkl', 'rb') as fb:
            userD = pickle.load(fb)

    if 'USER_DICT' in userD:
        print("ADDING NEW USER")
        userD['USER_DICT'].append({username: (password, priv, pub)})

    else:
        userD = {'USER_DICT': [{username: (password, priv, pub)}]}

    with open('UserDB.pkl', 'wb') as fw:
        pickle.dump(userD, fw)

    #print(userD)

if __name__ == '__main__':
    main()

