function e006() {
  const sum = (arr: number[]) => arr.reduce((s, i) => s + i, 0);

  const naturalNumbers: number[] = [];
  for (let i = 1; i <= 100; i++) {
    naturalNumbers.push(i);
  }

  const a = sum(naturalNumbers.map(i => i ** 2));
  const b = sum(naturalNumbers);

  let answer = b ** 2 - a;
  console.log(answer);
}

e006();
