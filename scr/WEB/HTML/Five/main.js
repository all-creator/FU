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
// 6
function range(a, b, c = 1){
    let arr = [];
    let j = 0;
    if (a < b){
        for (let i = 0; i < (b-a) + 1; i += c){
            arr[j] = i+a;
            j++;
        }
    }
    else{
        for (let i =(a-b+1); i > 0; i += c){
            arr[j] = i+b-1;
            j++;
        }
    }
    return arr;

}

function summ(arr){
    let sum = 0;
    for (let i of arr){
        sum += arr[i];
    }
    return sum;
}

let array = (range(1,54,53));
console.log(array);
console.log(summ(array));

// 7
function reverseArray(arr){
    n_arr = [];
    let j = 0;
    for (let i = arr.length-1; i > -1; i--){
        n_arr[j] = arr[i];
        j++;
    }
    return n_arr;
}

console.log(reverseArray([1,2,3,4,5]));

function reverseArrayInPlace(arr){
    for (let i = 0; i < arr.length/2; i++){
        let t = arr[i];
        arr[i] = arr[arr.length - i - 1];
        arr[arr.length - i - 1] = t;
    }
    return arr;
}

console.log(reverseArrayInPlace([1,2,3,4,5,6,7,8,12]));

// 8
let arr = [1,2,3,4,5,6,7]
function arrayToList(array){
    let list = {};
    for (let i of array){
        list = {
            value: Number(array[i]), rest: list
        };
    }
    return list
}

console.log(arrayToList(arr))