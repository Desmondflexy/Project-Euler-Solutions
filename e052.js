// Problem 52: Permuted multiples

/**Sort the number string */
const f = (n) => Array.from(n.toString()).sort().join('');
let x = 1;
while (true) {
    if (f(2 * x) === f(3 * x)
        && f(2 * x) === f(4 * x)
        && f(2 * x) === f(5 * x)
        && f(2 * x) === f(6 * x)) {
        console.log(x); break;
    }
    x++;
}