const {primes, reverse, isprime} = require('./myfunc');

const P = primes(5000000);
let s = k = 0;
for (let i = 0; i < P.length; i++) {
    const n = P[i]**2;
    const m = reverse(n);
    if (n !== m) {
        const r = Math.sqrt(m);
        if (r === Math.floor(r) && isprime(r)) {
            k++;
            s += n;
        }
        if (k === 50) break;
    }
}
console.log(s);
