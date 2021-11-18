// 1
let s = "#"
for (let i = 1; i <= 5; i++) {
    console.log(s)
    s += "#"
}
// 2
for (let i = 1; i <= 100; i++) {
    if (i % 5 ===0 || i % 3 === 0) {
        console.log("FizzBuzz")
    } else console.log(i)
}
// 3
for (let i = 0; i < 8; i++) {
    let s = ""
    if (i % 2 === 0) {
        for (let j = 0; j < 8; j++) {
            if (j % 2 === 0) {
                s += " "
            } else s += "#"
        }
    } else {
        for (let j = 0; j < 8; j++) {
            if (j % 2 === 0) {
                s += "#"
            } else s += " "
        }
    }
    console.log(s)
}
// 4
function min(f, s) {
    if (f > s) return s;
    else return f;
}
console.log(min(2, 1))
// 5
function countChar(str, char) {
    let c = 0;
    for (let i = 0; i < str.length; i++) {
        if (char === str.charAt(i)) c++;
    }
    return c;
}
function countBs(str) {
    return countChar(str, "B")
}
countBs("BBRTBB")