// import {reverse} from "./myfunc.js";

let largest = 0;
let c, pal;
for (let a = 900; a < 1000; a++) {
    for (let b = 900; b < 1000; b++) {
        c = a * b;
        if (c === reverse(c)) {
            pal = c;
            if (pal > largest) {
                largest = pal;
            }
        }
    }
}
console.log(largest);


/** Reverses the digits of a number */
function reverse(num) {
    let a = 0;
    while (num > 0) {
        a = a * 10 + num % 10;
        num = Math.floor(num / 10);
    }
    return a;
}