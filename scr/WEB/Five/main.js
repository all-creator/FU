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

// 9

function deepEqual(o1, o2){
    if (Object.keys(o1).length !== Object.keys(o2).length){
        return false;
    }

    for (let key of Object.keys(o1)){
        if ((isObj(o1[key]) && isObj(o2[key])) && !deepEqual(o1[key], o2[key])
            || !(isObj(o1[key]) || isObj(o2[key]))  && o1[key] !== o2[key]){
            return false;
        }
    }
    return true;
}

function isObj(val){
    return typeof val === 'object' && val != null;
}

const test_deep = {
    'x': {
        'y': {
            'z': 'your',
            'r': 'beer',
        },
        'x': {
            'a': 'test'
        }
    },
    'y': 'value'
};

const test_deep2 = test_deep.y = "test";

console.log(deepEqual(test_deep, test_deep));
console.log(deepEqual(test_deep, test_deep2));

// 10

let a = [[1,3,7], [2,4,5], [54,13,42], [1], [200,300]];
let d = a.reduce(function(arr, subarr){
    return arr.concat(subarr);
});

console.log(d)

// 11

function avg(arr){
    function plus(a,b) {return a+b;}
    return arr.reduce(plus) / arr.length;
}

let ANCESTRY_FILE = [
    {
        "name": "Carolus Haverbeke",
        "sex": "m",
        "born": 1832,
        "died": 1905,
        "father": "Carel Haverbeke",
        "mother": "Maria van Brussel"
    },
    {
        "name": "Emma de Milliano",
        "sex": "f",
        "born": 1876,
        "died": 1956,
        "father": "Petrus de Milliano",
        "mother": "Sophia van Damme"
    },
    {
        "name": "Maria de Rycke",
        "sex": "f",
        "born": 1683,
        "died": 1724,
        "father": "Frederik de Rycke",
        "mother": "Laurentia van Vlaenderen"
    },
    {
        "name": "Jan van Brussel",
        "sex": "m",
        "born": 1714,
        "died": 1748,
        "father": "Jacobus van Brussel",
        "mother": "Joanna van Rooten"
    },
    {
        "name": "Philibert Haverbeke",
        "sex": "m",
        "born": 1907,
        "died": 1997,
        "father": "Emile Haverbeke",
        "mother": "Emma de Milliano"
    },
    {
        "name": "Jan Frans van Brussel",
        "sex": "m",
        "born": 1761,
        "died": 1833,
        "father": "Jacobus Bernardus van Brussel",
        "mother": null
    },
    {
        "name": "Pauwels van Haverbeke",
        "sex": "m",
        "born": 1535,
        "died": 1582,
        "father": "N. van Haverbeke",
        "mother": null
    },
    {
        "name": "Clara Aernoudts",
        "sex": "f",
        "born": 1918,
        "died": 2012,
        "father": "Henry Aernoudts",
        "mother": "Sidonie Coene"
    },
    {
        "name": "Emile Haverbeke",
        "sex": "m",
        "born": 1877,
        "died": 1968,
        "father": "Carolus Haverbeke",
        "mother": "Maria Sturm"
    },
    {
        "name": "Lieven de Causmaecker",
        "sex": "m",
        "born": 1696,
        "died": 1724,
        "father": "Carel de Causmaecker",
        "mother": "Joanna Claes"
    },
    {
        "name": "Pieter Haverbeke",
        "sex": "m",
        "born": 1602,
        "died": 1642,
        "father": "Lieven van Haverbeke",
        "mother": null
    },
    {
        "name": "Livina Haverbeke",
        "sex": "f",
        "born": 1692,
        "died": 1743,
        "father": "Daniel Haverbeke",
        "mother": "Joanna de Pape"
    },
    {
        "name": "Pieter Bernard Haverbeke",
        "sex": "m",
        "born": 1695,
        "died": 1762,
        "father": "Willem Haverbeke",
        "mother": "Petronella Wauters"
    },
    {
        "name": "Lieven van Haverbeke",
        "sex": "m",
        "born": 1570,
        "died": 1636,
        "father": "Pauwels van Haverbeke",
        "mother": "Lievijne Jans"
    },
    {
        "name": "Joanna de Causmaecker",
        "sex": "f",
        "born": 1762,
        "died": 1807,
        "father": "Bernardus de Causmaecker",
        "mother": null
    },
    {
        "name": "Willem Haverbeke",
        "sex": "m",
        "born": 1668,
        "died": 1731,
        "father": "Lieven Haverbeke",
        "mother": "Elisabeth Hercke"
    },
    {
        "name": "Pieter Antone Haverbeke",
        "sex": "m",
        "born": 1753,
        "died": 1798,
        "father": "Jan Francies Haverbeke",
        "mother": "Petronella de Decker"
    },
    {
        "name": "Maria van Brussel",
        "sex": "f",
        "born": 1801,
        "died": 1834,
        "father": "Jan Frans van Brussel",
        "mother": "Joanna de Causmaecker"
    },
    {
        "name": "Angela Haverbeke",
        "sex": "f",
        "born": 1728,
        "died": 1734,
        "father": "Pieter Bernard Haverbeke",
        "mother": "Livina de Vrieze"
    },
    {
        "name": "Elisabeth Haverbeke",
        "sex": "f",
        "born": 1711,
        "died": 1754,
        "father": "Jan Haverbeke",
        "mother": "Maria de Rycke"
    },
    {"name": "Lievijne Jans", "sex": "f", "born": 1542, "died": 1582, "father": null, "mother": null},
    {
        "name": "Bernardus de Causmaecker",
        "sex": "m",
        "born": 1721,
        "died": 1789,
        "father": "Lieven de Causmaecker",
        "mother": "Livina Haverbeke"
    },
    {
        "name": "Jacoba Lammens",
        "sex": "f",
        "born": 1699,
        "died": 1740,
        "father": "Lieven Lammens",
        "mother": "Livina de Vrieze"
    },
    {
        "name": "Pieter de Decker",
        "sex": "m",
        "born": 1705,
        "died": 1780,
        "father": "Joos de Decker",
        "mother": "Petronella van de Steene"
    },
    {
        "name": "Joanna de Pape",
        "sex": "f",
        "born": 1654,
        "died": 1723,
        "father": "Vincent de Pape",
        "mother": "Petronella Wauters"
    },
    {
        "name": "Daniel Haverbeke",
        "sex": "m",
        "born": 1652,
        "died": 1723,
        "father": "Lieven Haverbeke",
        "mother": "Elisabeth Hercke"
    },
    {
        "name": "Lieven Haverbeke",
        "sex": "m",
        "born": 1631,
        "died": 1676,
        "father": "Pieter Haverbeke",
        "mother": "Anna van Hecke"
    },
    {
        "name": "Martina de Pape",
        "sex": "f",
        "born": 1666,
        "died": 1727,
        "father": "Vincent de Pape",
        "mother": "Petronella Wauters"
    },
    {
        "name": "Jan Francies Haverbeke",
        "sex": "m",
        "born": 1725,
        "died": 1779,
        "father": "Pieter Bernard Haverbeke",
        "mother": "Livina de Vrieze"
    },
    {
        "name": "Maria Haverbeke",
        "sex": "m",
        "born": 1905,
        "died": 1997,
        "father": "Emile Haverbeke",
        "mother": "Emma de Milliano"
    },
    {
        "name": "Petronella de Decker",
        "sex": "f",
        "born": 1731,
        "died": 1781,
        "father": "Pieter de Decker",
        "mother": "Livina Haverbeke"
    },
    {
        "name": "Livina Sierens",
        "sex": "f",
        "born": 1761,
        "died": 1826,
        "father": "Jan Sierens",
        "mother": "Maria van Waes"
    },
    {
        "name": "Laurentia Haverbeke",
        "sex": "f",
        "born": 1710,
        "died": 1786,
        "father": "Jan Haverbeke",
        "mother": "Maria de Rycke"
    },
    {
        "name": "Carel Haverbeke",
        "sex": "m",
        "born": 1796,
        "died": 1837,
        "father": "Pieter Antone Haverbeke",
        "mother": "Livina Sierens"
    },
    {
        "name": "Elisabeth Hercke",
        "sex": "f",
        "born": 1632,
        "died": 1674,
        "father": "Willem Hercke",
        "mother": "Margriet de Brabander"
    },
    {
        "name": "Jan Haverbeke",
        "sex": "m",
        "born": 1671,
        "died": 1731,
        "father": "Lieven Haverbeke",
        "mother": "Elisabeth Hercke"
    },
    {
        "name": "Anna van Hecke",
        "sex": "f",
        "born": 1607,
        "died": 1670,
        "father": "Paschasius van Hecke",
        "mother": "Martijntken Beelaert"
    },
    {
        "name": "Maria Sturm",
        "sex": "f",
        "born": 1835,
        "died": 1917,
        "father": "Charles Sturm",
        "mother": "Seraphina Spelier"
    },
    {
        "name": "Jacobus Bernardus van Brussel",
        "sex": "m",
        "born": 1736,
        "died": 1809,
        "father": "Jan van Brussel",
        "mother": "Elisabeth Haverbeke"
    }
];

let subs = [];
ANCESTRY_FILE.forEach(function(person){
    ANCESTRY_FILE.forEach(function(child){
        if (child.mother === person.name){
            subs.push(child.born - person.born);
        }
    })
});

console.log(avg(subs));

// 12

let centuriesAge = {};
ANCESTRY_FILE.forEach(function(person){
    if (centuriesAge[Math.ceil(person.died/100) + ' century'] === undefined){
        centuriesAge[Math.ceil(person.died/100) + ' century'] = [person.died-person.born];
    } else{
        centuriesAge[Math.ceil(person.died/100) + ' century'].push(person.died-person.born);
    }
});

for (let key of Object.keys(centuriesAge)){
    centuriesAge[key] = avg(centuriesAge[key]) + ' years';
}

console.log(centuriesAge);

// 13

function myEvery(array, func){
    let i = 0;
    while(i < array.length){
        if (!func(array[i])) return false;
        i++;
    }
    return true;
}

function mySome(array, func){
    let i = 0;
    while(i < array.length){
        if (func(array[i])) return true;
        i++;
    }
    return false;
}

console.log(myEvery([NaN,NaN,NaN],isNaN));
console.log(myEvery([NaN,NaN,4],isNaN));

console.log(mySome([2,2,NaN,2,1],isNaN));
console.log(mySome([2,2,2,2,2],isNaN));
