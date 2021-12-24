let date = new Date(2045, 0, 1, 0, 0, 0);

let data_naw = Date.now() / 1000;

function getDays(y, m) {
    return new Date(y,m,0).getDate();
}

console.log('18\n');
console.log(date);
console.log('19\n');
console.log(data_naw + ' s');
console.log('20\n');
console.log(getDays(2002, 0o1) + ' days');
console.log(getDays(2102, 0o2) + ' days');
console.log(getDays(2008, 0o2) + ' days');
console.log(getDays(2023, 0o2) + ' days');