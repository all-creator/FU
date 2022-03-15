console.log('22\n');

Number.prototype.isOdd = function(){
    return this % 2 !== 0;
}

let a = Number(3);
let b = Number(8);
console.log(a.isOdd());
console.log(b.isOdd());
