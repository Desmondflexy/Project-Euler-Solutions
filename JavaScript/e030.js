function sumpow(num, p = 5) {
    const digits = Array.from(num.toString());
    let sum = 0;
    digits.forEach(x => {
        sum += x ** p;
    })
    return sum;
}
let sum = 0;
for (let i = 4000; i <= 200000; i++) {
    if (i === sumpow(i)) {
        sum += i;
    }
}
console.log(sum);


