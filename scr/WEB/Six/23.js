console.log('23\n');

function Chain(val){
    this.val = val;
    this.add = function(a){
        this.val += a;
        return this;
    };
    this.substract = function(a){
        this.val -= a;
        return this;
    };
    this.multiply = function(a){
        this.val *= a;
        return this;
    };
    this.div = function(a){
        this.val /= a;
        return this;
    }
}

let example = new Chain(10).add(5).substract(7).multiply(3).div(8);
console.log(example.val);