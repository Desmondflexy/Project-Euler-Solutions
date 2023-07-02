e009();

function e009() {
  let c:number;
  let answer:number = 0;
  for (let b = 4; b < 1000; b++) {
    for (let a = 1; a <= b; a++) {
      c = Math.sqrt(a ** 2 + b ** 2);
      if (c === Math.floor(c) && a + b + c === 1000) {
        answer = a * b * Math.floor(c);
        break;
      }
    }
  }
  console.log(answer);
}