from flask import Flask, render_template, request, session, flash
from passlib.hash import sha256_crypt as sha
import configparser as cf
import json
import pickle
import hashlib
from create_account import createPass
import yao_test as yao

config = cf.ConfigParser()
config.read('config.ini')

port = config['DEFAULT']['PORT']
host = config['DEFAULT']['HOST']
tournieId = ""

app = Flask(__name__)
app.secret_key = b'(0a$li*&$p]/nap993-1z[1'

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/verify_login/', methods=['GET','POST'])
def verify_login():
    #result = [0, 0, 0]
    result = None

    checkUser, checkPass = False, False
    if 'username' in request.form and 'password' in request.form:

        '''
        text = "teto"
        valeur = hashlib.sha256(text.encode('utf-8')).hexdigest()
        if(valeur == request.form['username']):
            print('It is checked')
        else:
            print('error sha256 is different')

        #print(request.form['username'], '   ::   ', valeur)
        '''

        with open('UserDB.pkl', 'rb') as fr:
            dd = pickle.load(fr)

        for tup in dd['USER_DICT']:
            for key, val in tup.items():
                checkUser = sha.verify(request.form['username'], key)
                if checkUser == True:
                    checkPass = sha.verify(request.form['password'], val[0])

                if checkUser == True and checkPass == True:
                    with open('Keys.pkl', 'rb') as fr:
                        keys = pickle.load(fr)
                        pub = keys['KEY_DICT'][0]
                        print(pub.n)
                    session['username'] = request.form['username']
                    return render_template('auction.html', username=request.form['username'], result = result, public_key=[pub.n, pub.e])

        if checkUser == False and checkPass == False:
            return render_template('login.html',error='Wrong Username/Password')

    return render_template('login.html')


@app.route('/get_auctions/', methods=['GET','POST'])
def refresh_tourney():
    if 'username' not in session:
        return "You are not logged in <br><a href = '/'></b>" + "click here to log in</b></a>"

    return render_template('login.html')
    #return render_template('index.html', tourn_id = tournieId, eventList = jData['eventList'], blueTeam = blueTeam, redTeam = redTeam)




@app.route('/trial/', methods=['GET', 'POST'])
def create():
    return render_template('trial.html')

@app.route('/create_account/', methods=['GET', 'POST'])
def create_account():

    createPass(request.form['username'], request.form['password'])
    flash('Your account have been created successfully.')
    return render_template('login.html')


@app.route('/updateBid/', methods=['GET', 'POST'])
def updateBid():

    if 'bid' in request.form and 'publicKey' in request.form and 'bidid' in request.form:

        print("bid is ", request.form['bid'])
        bid = request.form['bid'];
        item = "x1" #get client session name so it is identified
        time = 0 #get the time when bid was made

        with open('BidDB.pkl', 'rb') as fr:
            bids = pickle.load(fr)
        with open('UserDB.pkl', 'rb') as f:
            users = pickle.load(f)

        if 'BIDS' in users:
            print("Updating Bids")
            users['BIDS'].append({item: (bid, time)})

        else:
            users = {'BIDS': [{item: (bid, time)}]}



        for keys in users['USER_DICT']:
            #should check if given public key exist and is the same as the user's
            for key in keys.items():
                #when key found look at the bids

                for tup in bids['BIDS']:
                    for val in tup.items():
                        #Place bid in file and compare to other
                        return render_template('auction.html')
        return render_template('auction.html')
    return render_template('auction.html')


@app.route('/checkRSA/', methods=['GET', 'POST'])
def check():
    result = None

    with open('Keys.pkl', 'rb') as fr:
        keys = pickle.load(fr)
        pub = keys['KEY_DICT'][0]
        priv = keys['KEY_DICT'][1]

    a = 55
    if 'val' in request.form:
        d = yao.serverSide(a, int(request.form["val"]));
        print("HERE IS X",int(request.form["val"]))
        result = d 
        print("Giving",result)
    return render_template('auction.html', result = result, public_key=[pub.n, pub.e])

@app.route('/refresh/', methods=['GET', 'POST'])
def refresh():

    #update infos
    return render_template('auction.html')


if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
