// Problem 45: Triangular, pentagonal, and hexagonal

const T = (n) => n * (n + 1) / 2;
const P = (n) => n * (3 * n - 1) / 2;
const H = (n) => n * (2 * n - 1);

/**Find the next occurence of t = T(x) = P(y) = H(z). */
function find_next(pos) {
    let [x, y, z] = pos.map(i => i + 1);
    while (true) {
        const h = H(z);
        while (P(y) <= h) {
            const p = P(y);
            if (p == h) {
                while (T(x) <= p) {
                    const t = T(x);
                    if (t == p) {
                        return [x, y, z];
                    }
                    x++;
                }
            }
            y++;
        }
        z++;
    }
}
console.log(`Answer: ${T(find_next([285, 165, 143])[0])}`);