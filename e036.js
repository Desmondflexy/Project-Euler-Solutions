/**Checks if a number is palindrome */
function ispal(n) {
    let a = Array.from(n.toString());
    let b = a.map(i => i).reverse();
    return a.toString() === b.toString();
}

let sum = 0;
for (let i = 1; i < 1000000; i = i + 2) {
    if (ispal(i) && ispal(i.toString(2))) sum += i;
}
console.log(sum);