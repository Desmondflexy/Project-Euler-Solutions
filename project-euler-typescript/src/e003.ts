function e003() {
  let value: number = 600851475143;
  for (let i = 2; i < value; i++) {
    if (value % i === 0) {
      value /= i;
    }
  }
  console.log(value);
}

e003();