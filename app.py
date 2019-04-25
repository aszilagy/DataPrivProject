from flask import Flask, render_template, request, session
from passlib.hash import sha256_crypt as sha
import configparser as cf
import json
import pickle

config = cf.ConfigParser()
config.read('config.ini')

with open('UserDB.pkl', 'rb') as fb:
    userDB = pickle.load(fb)

port = config['DEFAULT']['PORT']
host = config['DEFAULT']['HOST']
tournieId = ""

app = Flask(__name__)
app.secret_key = b'(0a$li*&$p]/nap993-1z[1'

@app.route('/', methods=['GET'])
def login():
    print(userDB)
    return render_template('login.html')

@app.route('/verify_login/', methods=['GET','POST'])
def verify_login():
    if 'username' in request.form and 'password' in request.form:
        with open('UserDB.pkl', 'wb') as fw:
            pickle.dump(userD, fw)

        for key, val in dd.items():
            checkUser = sha.verify(request.form['username'], key)
            if checkUser == True:
                checkPass = sha.verify(request.form['password'], val)

                if checkUser == True and checkPass == True:
                    session['username'] = request.form['username']
                    return render_template('index.html', username=request.form['username'])

        if checkUser == False or checkPass == False:
            return render_template('login.html',error='Wrong Username/Password')

    return render_template('login.html')

@app.route('/get_auctions/', methods=['GET','POST'])
def refresh_tourney():
    if 'username' not in session:
        return "You are not logged in <br><a href = '/'></b>" + "click here to log in</b></a>"

    return render_template('index.html')
    #return render_template('index.html', tourn_id = tournieId, eventList = jData['eventList'], blueTeam = blueTeam, redTeam = redTeam)


if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
