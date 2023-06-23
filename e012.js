const {ndivs} = require('./myfunc');

let k = 0, t = 0, i = 1;
for (let n = 1; k <= 500; n++) {
  t += i;
  k = ndivs(t);
  i++;
}
console.log(t);
