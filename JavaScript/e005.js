let multiple = maxdivisor = 20;
  let notfound = true;

  while (true) {
    for (let i = 1; i <= maxdivisor; i++) {
      if (multiple % i !== 0) {
        notfound = false;
        break;
      }
    }
    if (notfound) {
      break;
    }
    multiple += maxdivisor;
    notfound = true;
  }
  console.log(multiple);
