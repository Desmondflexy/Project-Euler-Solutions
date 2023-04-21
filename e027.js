function formlen(a, b) {
    let n = 0, p;
    while (true) {
        p = n * n + a * n + b;
        if (p <= 0) { return 0 };
        if (isprime(p)) {
            n += 1;
        } else {
            break;
        }
    }
    return n;
}

const limit = 1000;
const b_list = primes(limit);
let cmax = 0, A, B;
for (let a = -limit + 1; a < limit; a += 2) {
    b_list.forEach(b => {
        let c = formlen(a, b);
        if (c > cmax) {
            [A, B, cmax] = [a, b, c];
        }
    })
}
const answer = A * B;
console.log(answer);


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