// 7
let d_1 = [45, 78, 10, 3];
d_1[7] = 100;
console.log("Массив: ", d_1);
console.log("Элементы 6 и 7: ", d_1[6], ",", d_1[7]);

// 8
let d_2 = [45, 78, 10, 3];
let sum2 = 0;
for (let i of d_2.length) {
    sum2 += d_2[i];
}
console.log("Сумма массива d_2: ", sum2);

// 9
let d_3 = [45, 78, 10, 3];
d_3[7] = 100;
let sum3 = 0;
for (const elem in d_3) {
    sum3 += elem;
}
console.log("Сумма массива d_3: ", sum3);

// 10
let d_4 = [45, 78, 10, 3];

function my(a, b) {
    return a > b ? -1 : 1;
}

console.log("Отсортированный по убыванию d_4: ", d_4.sort(my));

// 11
let d_5 = [];
for (let i = 0; i < 3; i++) {
    d_5[i] = [];
    for (let j = 0; j < 4; j++) {
        d_5[i].push(5);
    }
}
console.log("Двумерный d_5, сгенерированный циклами", d_5);