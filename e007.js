let counter = 1;
let n = 2;
while (counter < 10001) {
    n += 1;
    if (isprime(n)) {
        counter++;
    }
}
let answer = n;
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