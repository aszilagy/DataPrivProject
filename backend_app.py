import requests
import time
import json
import urllib
from pprint import pprint
import flask
import configparser as cf

config = cf.ConfigParser()
config.read('config.ini')

def main():
    start = time.time()
    end = time.time()
    print("MAIN TOOK %.2gs" % (end-start))

def jprint(jsonD):
    '''
    Parameters: Request ... myReq  [Returned from requests.get]
    '''
    jData = json.loads(jsonD.content)
    print(jData)

if __name__ == '__main__':
    main()
