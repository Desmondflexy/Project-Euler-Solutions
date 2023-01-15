function factorial(n){
    let p = 1;
    for (let i = n; i >= 1; i--){
        p *= i;
    }
    return p;
}

function sumfac(num){
    const digits = Array.from(num.toString());
    let sum = 0;
    digits.forEach(x => sum += factorial(x));
    // console.log(digits);
    return sum;
}

let s = 0;
for (let n = 3; n < 10000000; n++){
    if (n === sumfac(n)){
        console.log(n);
        s += n;
    }
}
console.log(s);