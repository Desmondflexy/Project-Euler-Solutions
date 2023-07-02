import { isprime } from "./myfunc.js";

e007();

function e007() {
  let counter = 1;
  let n = 2;
  while (counter < 10001) {
    n += 1;
    if (isprime(n)) {
      counter++;
    }
  }
  console.log(n);
}