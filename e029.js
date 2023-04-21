const ylist = [];
for (let a = 2; a <= 100; a++) {
    for (let b = 2; b <= 100; b++) {
        const y = a ** b;
        if (!ylist.includes(y)) {
            ylist.push(y);
        }
    }
}
console.log(ylist.length);
