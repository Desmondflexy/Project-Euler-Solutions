
let count = 0;
for (let start = 1; start < 10000000; start++) {
    let n = start;
    while (!(n === 1 || n === 89)) n = func(n);
    if (n === 89) count++;
}
console.log(`Arrived at eighty-nine ${count} times.`);

/**Add square of digits */
function func(n) {
    let sum = 0;
    const m = Array.from(n.toString()).map(i => i**2);
    m.forEach(i => sum += i);
    return sum;
}