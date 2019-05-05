from simpleRSA import *
import random

public_key, private_key = make_key_pair(12)  # safe for n<100


A = random.randint(1,9)
B = random.randint(1,9)

def safeCmpAleB(a,b):
    print("\nA has i={} millions and B has j={} millions".format(a,b))
    print("\nA generate a pair of RSA key:")
    print("The public key is {}, which is shared in public".format(public_key))
    print("The private key is {}, which is only hold by A\n".format(private_key))
    x = random.randint(1000,2000)
    print("Step 1:   B generate a large random number: ".format(x))
    K = public_key.encrypt(x)
    print("\tB encryt it with the shared public key to generate a cipher K: ".format(K))
    print("\tthen B send c=K-j({}-{}={} to A\n".format(K,b,K-b))
    c = K - b  
    p=29
    d=[]
    for i in range(c+1,c+11):
        d.append( (private_key.decrypt(i) % p))
    print("Step 2:   A decrypt c+1,...c+10 with his own private key:" ) 
    print("\t{}".format(d)) 
    for i in range(a,10):
        d[i]=d[i]+1
    print("\n\tA add 1 to c+i+1 to c+10:" ) 
    print("\t{}".format(d))
    print("\nStep 3:   B test whether x mod p equals to d[j]. \n\tif so, i>=j\n\totherwise,i<j\n")
    print("d[j] is {}, x mod p is {}".format(d[b-1],x%p))
    if(x%p==d[b-1]):
        return True
    else:
        return False
    
print(safeCmpAleB(A,B))
print(A>=B)
