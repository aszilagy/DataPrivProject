/**
 * RSA hash function reference implementation.
 * Uses BigInteger.js https://github.com/peterolson/BigInteger.js
 * Code originally based on https://github.com/kubrickology/Bitcoin-explained/blob/master/RSA.js
 */


/**
 * Generates a k-bit RSA public/private key pair
 * https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Code
 *
 * @param   {keysize} int, bitlength of desired RSA modulus n (should be even)
 * @returns {array} Result of RSA generation (object with three bigInt members: n, e, d)
 */
function generate() {

   var keyS = 32
  // set up variables for key generation
  const e = bigInt(65537);  // use fixed public exponent
  let p;
  let q;
  let lambda;

  // generate p and q such that λ(n) = lcm(p − 1, q − 1) is coprime with e and |p-q| >= 2^(keysize/2 - 100)
  do {
    p = randomPrime(keyS / 2);
    q = randomPrime(keyS / 2);
    lambda = bigInt.lcm(p.minus(1), q.minus(1));
  } while (bigInt.gcd(e, lambda).notEquals(1) || p.minus(q).abs().shiftRight(keyS / 2 - 100).isZero());
  return {
    n: p.multiply(q),  // public key (part I)
    e: e,  // public key (part II)
    d: e.modInv(lambda),  // private key d = e^(-1) mod λ(n)
  };
};

/**
   * Generates a random k-bit prime greater than √2 × 2^(k-1)
   *
   * @param   {bits} int, bitlength of desired prime
   * @returns {bigInt} a random generated prime
   */
function randomPrime(bits) {
    const min = bigInt(6074001000).shiftLeft(bits - 33);  // min ≈ √2 × 2^(bits - 1)
    const max = bigInt.one.shiftLeft(bits).minus(1);  // max = 2^(bits) - 1
    for (;;) {
      const p = bigInt.randBetween(min, max);  // WARNING: not a cryptographically secure RNG!
      if (p.isProbablePrime(256)) {
        return p;
      }
    }
};


/**
 * Encrypt
 *
 * @param   {m} int / bigInt: the 'message' to be encoded
 * @param   {n} int / bigInt: n value returned from RSA.generate() aka public key (part I)
 * @param   {e} int / bigInt: e value returned from RSA.generate() aka public key (part II)
 * @returns {bigInt} encrypted message
 */
function encrypt(m, n, e) {
  return bigInt(m).modPow(e, n);
};





/**
 * Decrypt
 *
 * @param   {c} int / bigInt: the 'message' to be decoded (encoded with RSA.encrypt())
 * @param   {d} int / bigInt: d value returned from RSA.generate() aka private key
 * @param   {n} int / bigInt: n value returned from RSA.generate() aka public key (part I)
 * @returns {bigInt} decrypted message
 */
function decrypt(c, d, n) {
  return bigInt(c).modPow(d, n);
};










