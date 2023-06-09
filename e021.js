function sumdivs(num) {
    let sum = 0;
    divisors(num).forEach(i => sum += i);
    return sum - num;
}

let S = 0;
for (let a = 2; a <= 10000; a++) {
    const b = sumdivs(a);
    if (sumdivs(b) === a && a !== b) {
        S += a;
    }
}
console.log(S);


function divisors(n) {
    let A = [], B = [];
    let a = 0, b = 0;
    for (let i = 1; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            a = i;
            b = parseInt(n / i);
            A = [...A, a];
            B = [...B, b];
        }
    }
    if (a === b) {
        B.pop();
    }
    B.reverse();
    return [...A, ...B];
}