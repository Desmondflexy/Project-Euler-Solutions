function CodelandUsernameValidation(str) {
    // code goes here  
    // const valid_reg = /^[A-Za-z]\w+[A-Za-z0-9]$/;
    // const valid_length = (str) => str.length >= 4 && str.length <= 25;
    // return valid_reg.test(str) && valid_length(str);
    console.log(str);
    const letters = [];
    for (let n = 65; n <= 90; n++) {
        const s = String.fromCharCode(n);
        letters.push(s, s.toLowerCase());
    }
    const numbers = [];
    for (let n = 0; n <= 9; n++) {
        numbers.push(n.toString());
    }
    let let_num_und = [...letters, ...numbers, '_'];

    if (str.length < 4) {
        console.log('error! must not be less than 4 characters!')
        return false;
    }
    if (str.length > 25) {
        console.log('error! must not be more than 25 characters.');
        return false;
    }
    if (!letters.includes(str[0])) {
        console.log('error! must start with a letter.');
        return false;
    }
    if (!Array.from(str).every(i => let_num_und.includes(i))) {
        console.log('Error! Contains invalid character.');
        return false;
    }
    if (str[str.length - 1] === '_'){
        console.log('Error! Cannot end with an underscore character.');
        return false;
    }
    return true;
}

// keep this function call here 
console.log(CodelandUsernameValidation('abcd_'));