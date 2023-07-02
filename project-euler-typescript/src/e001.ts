e001();

function e001() {
  let sum: number = 0;
  for (let num = 1; num < 1000; num++) {
    if (num % 3 === 0 || num % 5 === 0) {
      sum += num;
    }
  }
  console.log(sum);
}
