let city = {};
city.name = 'ГородN';
city.population = 10**6;
city.getName = getName;
city.exportStr = exportStr;
city.getCity = getObj;

let city_two = {
    name: 'ГородM',
    population: 1e6,
    getName: getName,
    exportStr: exportStr,
    getCity: getObj,
}

function getObj(){
    return this;
}
function getName(){
    return this.name;
}
function exportStr(){
    let s = '';
    for (let key in this){
        if (typeof this[key] != 'function'){
            s += key + '=' + this[key] + '\n';
        }
    }
    return s;
}

console.log('3\n');
console.log(city.getName(), city_two.getName());
console.log('4\n');
console.log(city.exportStr(), city_two.exportStr());
console.log('5\n');
console.log(city.getCity(), city_two.getCity());