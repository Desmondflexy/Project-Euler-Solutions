let k = 0, t = 0, i = 1;
for (let n = 1; k <= 500; n++) {
  t += i;
  k = ndivs(t);
  i++;
}
console.log(t);

function ndivs(n) {
  let k = 0;
  let z = Math.sqrt(n);
  for (let i = 1; i <= z; i++) {
    if (n % i === 0) k += 2;
  }
  if (z * z === n) k--;
  return k;
}