/** Reverses the digits of a number */
export function reverse(num: number): number {
  let a = 0;
  while (num > 0) {
    a = a * 10 + num % 10;
    num = Math.floor(num / 10);
  }
  return a;
}


/** Returns true if a number is prime */
export function isprime(n: number): boolean {

  if (n === 2 || n === 3) return true;
  if (n < 2 || n % 2 === 0) return false;
  if (n < 9) return true;
  if (n % 3 === 0) return false;

  let f = 5;
  while (f <= Math.floor(Math.sqrt(n))) {
    if (n % f === 0) return false;
    if (n % (f + 2) === 0) return false;
    f += 6;
  }
  return true;
}


/** Calculates sum of all elements in an array */
export function sum(array: number[]) {
  let s = 0;
  for (let i of array) {
    s += i;
  }
  return s;
}


/** Calculates number of divisors of a number */
export function ndivs(n: number) {
  let k = 0;
  let z = Math.sqrt(n);
  for (let i = 1; i <= z; i++) {
    if (n % i === 0) k += 2;
  }
  if (z * z === n) k--;
  return k;
}


/** Generates list of divisors of a number */
export function divisors(n: number) {
  let A: number[] = [], B: number[] = [];
  let a = 0, b = 0;
  for (let i = 1; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      a = i;
      b = Math.trunc(n / i);
      A = [...A, a];
      B = [...B, b];
    }
  }
  if (a === b) {
    B.pop();
  }
  B.reverse();
  return [...A, ...B];
}


/** Generates list of prime numbers up to n */
export function primes(n: number) {
  let p: number[] = [];
  for (let i = 1; i <= n; i += 2) {
    p.push(i);
  }
  let q = p.length;
  p[0] = 2;
  for (let k = 3; k <= Math.sqrt(n); k += 2) {
    if (p[Math.floor((k + 1) / 2 - 1)]) {
      for (let i = Math.floor((k * k + 1) / 2) - 1; i < q; i += k) {
        p[i] = 0;
      }
    }
  }
  return p.filter(i => i > 0);
}


/**Count the number of occurence in an array */
export function count(arr: any, elem: any): number {
  return arr.filter((i: any) => i === elem).length;
}


/**Converts text to proper case */
export function properCase(text:string) {
  const words = text.split(' ').map(word => {
    const firstLetter = word.substring(0, 1).toUpperCase();
    return firstLetter + word.substring(1);
  })
  return words.join(' ');
}


/**Gets the acronym of a text */
export function acronym(text:string) {
  return text.split(' ').map(word => word.substring(0, 1).toUpperCase()).join('');
}


export function factorial(n:number) {
  let p = 1;
  for (let i = n; i >= 1; i--) {
    p *= i;
  }
  return p;
}

// module.exports = {
//   reverse,
//   isprime,
//   sum,
//   ndivs,
//   divisors,
//   primes,
//   count,
//   properCase,
//   acronym,
//   factorial,
//   author: 'Desmond'
// }