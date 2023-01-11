let a = 1, b = 2, c, x = 0;
while (a < 4000000) {
    c = a + b;
    a = b;
    b = c;
    if (a % 2 === 0) {
        x += a;
    }
}
console.log(x);