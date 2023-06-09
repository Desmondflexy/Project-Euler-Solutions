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

let [n, count, s] = [11, 0, 0];
while (count < 11){
    if (isprime(n)){
        const a = n.toString();
        let k = 1;
        for (let i = 1; i<= a.length; i++){
            const nleft = Number(a.slice(i));
            const nright = Number(a.slice(0,i));
            if (isprime(nleft) && isprime(nright)) k += 1;
            else break;
        }
        if (k === a.length){
            s += n;
            count += 1;
            console.log(n)
        }
    }
    n += 2;
}
console.log(s);