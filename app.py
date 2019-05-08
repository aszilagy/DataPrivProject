from flask import Flask, render_template, request, session, flash
from passlib.hash import sha256_crypt as sha
import configparser as cf
import json
import pickle
import hashlib
from create_account import createPass

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
    result = [0, 0, 0]

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
                    session['username'] = request.form['username']
                    return render_template('auction.html', username=request.form['username'], result = result)

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
    print("Bid is : ", request.form["bid"])
    print("decrypt is : ", request.form["publicKey"])
    if 'val' in request.form:
        print("val is : ", request.form["val"])
    else:
        print("Didn't find val")

    if 'bid' in request.form:
        print("bid is : ", request.form["bid"])
        print("publicKey is : ", request.form["publicKey"])
    result = []
    return render_template('auction.html', result = result)




@app.route('/refresh/', methods=['GET', 'POST'])
def refresh():

    #update infos
    result = [request.form["lastname"]]
    return render_template('auction.html', result = result)









if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
