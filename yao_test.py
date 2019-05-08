from simpleRSA import *
import random
import sys

public_key, private_key = make_key_pair(12)  # safe for n<100

if len(sys.argv) < 3:
    print("python yao_test.py <userA_bid> <userB_bid>")
    sys.exit()


A = int(sys.argv[1]) #random.randint(1,9)
B = int(sys.argv[2]) #random.randint(1,9)
x = random.randint(1000,2000)

def main():
    #print("UserA bid is accepted:",safeCmpAleB(A,B))
    #print("UserA >= UserB:",A>=B)

    toServer = clientSide(B, x) #userBid, RandomVal

    serverResult = serverSide(A, toServer)

    print("Bid accepted:",clientResult(serverResult, B, x))


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


def safeCmpAleB(a,b):
    print("\nA bid is i={} and B bid is j={}".format(a,b))
    print("\nA generate a pair of RSA key:")
    print("The public key is {}, which is shared in public".format(public_key))
    print("The private key is {}, which is only hold by A\n".format(private_key))
    x = random.randint(1000,2000)
    print("Step 1:   B generate a large random number: ".format(x))
    K = public_key.encrypt(x)
    print("\tB encryt it with the shared public key to generate a cipher K: ".format(K))
    print("\tthen B send c=K-j = {}-{}={} to A\n".format(K,b,K-b))
    c = K - b  
    #SEND C TO SERVER
    p=29
    d=[]
    for i in range(c+1,c+1001):
        d.append( (private_key.decrypt(i) % p))
    print("Step 2:   A decrypt c+1,...c+10 with his own private key:" ) 
    print("\tDECRYPTED D: {}".format(d)) 
    for i in range(a,1000):
        d[i]=d[i]+1
    print("\n\tA add 1 to c+i+1 to c+10:" ) 
    print("\tAFTER ADD{}".format(d))
    print("\nStep 3:   B test whether x mod p equals to d[j]. \n\tif so, i>=j\n\totherwise,i<j\n")
    print("d[j] is {}, x mod p is {}".format(d[b-1],x%p))
    if(x%p==d[b-1]):
        return True
    else:
        return False

main()
