console.log('15\n');


function Card(from, to){
    this.from = from;
    this.to = to;
    this.show = function(){
        return `${this.from}, ${this.to}`;
    }
}

let c1 = new Card('Комсомольск-на-Амуре','Москва');
console.log(c1.show());
