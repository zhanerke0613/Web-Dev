let a = prompt("First number?", 1);
let b = prompt("Second number?", 2);

alert(a + b); // 12


// to fix this, we need to convert a and b to numbers

let a = prompt("First number?", 1);
let b = prompt("Second number?", 2);

alert(Number(a) + Number(b)); 

// the result is 3


