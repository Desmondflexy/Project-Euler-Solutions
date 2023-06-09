let countdays = 365, daysOfMonth, sum = 0;
for (let yyyy = 1901; yyyy <= 2000; yyyy++) {
    for (let mm = 0; mm < 12; mm++) {
        if (mm === 1) {  // February
            if (yyyy % 4 === 0 && yyyy % 100 !== 0 || yyyy % 400 === 0) {  // Leap year
                daysOfMonth = 29;
            } else { // other year
                daysOfMonth = 28;
            }
        } else if ([8, 3, 5, 10].includes(mm)) {
            daysOfMonth = 30;
        } else {
            daysOfMonth = 31;
        }
        for (let dd = 1; dd <= daysOfMonth; dd++) {
            countdays++;
            if (countdays % 7 === 0 && dd === 1) {
                sum++;
            }
        }
    }
}
console.log(sum);