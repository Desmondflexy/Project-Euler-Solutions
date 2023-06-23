// import {reverse} from "./myfunc.js";
const {reverse} = require('./myfunc')

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
