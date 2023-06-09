let a = 1, s = a;
const N = 1001;
for (let n = 3; n <= N; n += 2) {
    const d = n - 1;
    const v = [a + d, a + 2 * d, a + 3 * d, a + 4 * d];
    v.forEach(i => s += i);
    a = v[3];
}
console.log(s);