from simpleRSA import *
import random
import sys
import pickle

with open('Keys.pkl', 'rb') as fr:
    keys = pickle.load(fr)
    public_key = keys['KEY_DICT'][0]
    private_key = keys['KEY_DICT'][1]


def main():
    A = int(sys.argv[1]) #random.randint(1,9)

    B = int(sys.argv[2]) #random.randint(1,9)
    x = random.randint(1000,2000)
    #toServer = clientSide(B, x) #userBid, RandomVal
    #print(toServer)

    #serverResult = serverSide(A, toServer)

    #print("Bid accepted:",clientResult(serverResult, B, x))


def clientResult(d, b, x, p=29):
    print("\nStep 3:   B test whether x mod p equals to d[j]. \n\tif so, i>=j\n\totherwise,i<j\n")
    print("d[j] is {}, x mod p is {}".format(d[b-1],x%p))
    if(x%p==d[b-1]):
        return True
    else:
        return False


def serverSide(a, c):
    p=29
    d=[]
    for i in range(c+1,c+1001):
        d.append( (private_key.decrypt(i) % p))
    print("Step 2:   A decrypt c+1,...c+10 with his own private key:" ) 
    #print("\tDECRYPTED D: {}".format(d)) 
    for i in range(a,1000):
        d[i]=d[i]+1
    print("\n\tA add 1 to c+i+1 to c+10:" ) 
    #print("\tAFTER ADD{}".format(d))
    return d


def clientSide(b, x):
    print("Step 1:   B generate a large random number: ".format(x))
    K = public_key.encrypt(x)
    print("\tB encryt it with the shared public key to generate a cipher K: ".format(K))
    print("\tthen B send c=K-j = {}-{}={} to A\n".format(K,b,K-b))
    c = K - b  
    return c

if __name__ == '__main__':
    main()
