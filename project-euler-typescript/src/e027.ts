import { isprime, primes } from "./myfunc.js";

e027();

function e027() {
  function formlen(a: number, b: number) {
    let n = 0, p;
    while (true) {
      p = n * n + a * n + b;
      if (p <= 0) { return 0; };
      if (isprime(p)) {
        n += 1;
      } else {
        break;
      }
    }
    return n;
  }

  const limit = 1000;
  const b_list = primes(limit);
  let cmax = 0, A = 0, B = 0;
  for (let a = -limit + 1; a < limit; a += 2) {
    b_list.forEach(b => {
      let c = formlen(a, b);
      if (c > cmax) {
        [A, B, cmax] = [a, b, c];
      }
    });
  }
  const answer = A * B;
  console.log(answer);
}
