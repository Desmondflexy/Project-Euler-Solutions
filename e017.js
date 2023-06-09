const num2word = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eigtheen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
    80: 'eigthy', 90: 'ninety'
}
for (let T = 20; T < 100; T += 10) {
    for (let U = 1; U < 10; U++) {
        num2word[T + U] = num2word[T] + num2word[U];
    }
}
for (let H = 100; H < 1000; H += 100) {
    num2word[H] = num2word[H / 100] + 'hundred';
    for (let TU = 1; TU < 100; TU++) {
        num2word[H + TU] = num2word[H] + 'and' + num2word[TU]
    }
}
num2word[1000] = 'onethousand'
const word = Object.values(num2word);
let sum = 0;
for (let letter of word) {
    sum += letter.length;
}
console.log(sum);