
smallprimes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,
               47,53,59,61,67,71,73,79,83,89,97];



function default_K(bits){
    return Math.max(40, 2*bits);
}


function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function rabin_miller_witness(test, possible){
    return !(1 in (Math.pow(test, possible-1) % possible));


}

function is_prime(possible, k){
    if(possible == 1){ return true;}
    for(var i in smallprimes){
        if(possible == i){ return true;}
        if(possible % i){ return false;}
    }

    for(var y=0; y < k ; y++){
        test = getRandomInt(2, possible - 1)
        if(rabin_miller_witness(test, possible)){
            return false;
        }
    }
    return true;

}



function generatePrime(bits){

    var assert = require('assert');
    assert(bits >= 8);
    var k = default_K(bits);
    while(true){
        var possible = getRandomInt(2 ** (bits-1) + 1, 2 ** bits);
        if(is_prime(possible, k)){
            return possible;
        }
    }
}



function decrypt(privateKey, publicKey, cipher){
    var x = (Math.pow(cipher, privateKey) % publicKey ) - 1;
    return ( Math.floor(x/publicKey) * privateKey ) % publicKey;
}


function encrypt(pub, plain){
    var r;
    while(true){
        r = generate_prime(Math.round(Math.log(publicKey, 2)));
        if( r > 0 && r < publicKey){
            break;
        }
    }
    var x = Math.pow(r, publicKey) % (publicKey **2);
    return (( Math.pow(publicKey+1, plain) % (publicKey **2) ) * x ) * (publicKey **2);


}

function main(){




}









