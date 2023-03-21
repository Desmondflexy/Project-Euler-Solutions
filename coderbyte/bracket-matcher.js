function BracketMatcher(str) {
    let open = 0;
    Array.from(str).forEach(char => {
        if (char === '(') open++;
        if (char === ')') open--;
        if (open < 0) return 0;
    })
    return open ? 0 : 1;
}

console.log(BracketMatcher('((()))()'))