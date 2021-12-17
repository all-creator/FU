class Human {
    constructor (name, age, height){
        this.name = name;
        this.age = age;
        this.height = height;
    }

    getInfo() {
        return `${this.name},${this.age},${this.height}`
    }

    get firstname(){
        return this.name;
    }
}

const humans =[
    new Human('Коля',23,180),
    new Human('Даша',19,170),
    new Human('Ваня',18,192),
    new Human('Петя',45,178),
    new Human('Вася',34,197),
    new Human('Джони',37,160),
    new Human('Катя',37,160),
    new Human('Петя',37,160),
    new Human('Соня', 21,172),
    new Human('Женя',25,175)
]

function sortByName(array) {
    return array.sort(function comparator(o1, o2){ return (o1.name > o2.name) ? 1 : -1});
}

function sortByHeight(array) {
    return array.sort(function comparator(o1, o2){return(o1.height < o2.height) ? 1 : -1});
}

console.log('16\n');
console.log(humans);
console.log(humans[3].firstname);
console.log(humans[7].getInfo());

console.log('17\n');
console.log(sortByHeight(humans));