/** Generates list of prime numbers */
function primes(n) {
    let p = [];
    for (let i = 1; i <= n; i += 2) {
        p.push(i);
    }
    let q = p.length;
    p[0] = 2;
    for (let k = 3; k <= Math.sqrt(n); k += 2) {
        if (p[Math.floor((k + 1) / 2 - 1)]) {
            for (let i = Math.floor((k * k + 1) / 2) - 1; i < q; i += k) {
                p[i] = 0;
            }
        }
    }
    return p.filter(i => i > 0);
}

/** Reverses the digits of a number */
function reverse(num) {
    let a = 0;
    while (num > 0) {
        a = a * 10 + num % 10;
        num = Math.floor(num / 10);
    }
    return a;
}

/** Returns true if a number is prime */
function isprime(n) {
    if (n === 2 || n === 3) return true;
    if (n < 2 || n % 2 === 0) return false;
    if (n < 9) return true;
    if (n % 3 === 0) return false;

    let f = 5;
    while (f <= Math.floor(Math.sqrt(n))) {
        if (n % f === 0) return false;
        if (n % (f + 2) === 0) return false;
        f += 6;
    }
    return true;
}

const P = primes(50000000);
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