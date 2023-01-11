// import {sum} from "./myfunc.js";

const naturalNumbers = [];
for (let i = 1; i <= 100; i++) {
    naturalNumbers.push(i);
}

const a = sum(naturalNumbers.map(i => i ** 2));
const b = sum(naturalNumbers);

let answer = b ** 2 - a;
console.log(answer);

function sum(array) {
    let s = 0;
    array.forEach(i => {s += i});
    return s;
}