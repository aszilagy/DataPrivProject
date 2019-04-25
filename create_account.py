from passlib.hash import sha256_crypt as sha
import argparse
import sys
import paillier as pail
import configparser as cf
import json
import ast

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
    print(priv)

    config = cf.ConfigParser()
    config.read('pauser.tmp')

    if 'USER_DICT' in config['DEFAULT']:
        encrypted_dict = config['DEFAULT']['USER_DICT']

        en_dic = encrypted_dict.replace("'", "\"")
        en_dic = encrypted_dict.replace("\n", "")
        print(en_dic[81:83])
        userD = en_dic
        userD[username] = (password, priv, pub)
    else:
        userD = {username: (password, priv, pub)}


    with (open('pauser.tmp','w')) as fp:
        fp.write('[DEFAULT]\n')
        fp.write(f'USER={user}\n')
        fp.write(f'PASSWORD={pa}\n')
        fp.write('USER_DICT=' + str(userD) + '\n')
        fp.write(f'USER_ENCRYPT={username}\n')
        fp.write(f'PASSWORD_ENCRYPT={password}\n')
        fp.write(f'PRIV_KEY={priv}\n')
        fp.write(f'PUB_KEY={pub}\n')

if __name__ == '__main__':
    main()

