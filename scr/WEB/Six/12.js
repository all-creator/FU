console.log("12\n");
function Vector(x, y){
    this.x = x;
    this.y = y;
    this.plus = function (vector) {
        return new Vector(this.x + vector.x, this.y + vector.y);
    }
    this.minus = function (vector) {
        return new Vector(this.x - vector.x, this.y - vector.y);
    }
    this.length = function () {
        return Math.sqrt(x*x + y*y);
    }
}

console.log("Длина вектора: ", new Vector(3,4).length());
console.log("Сумма векторов: ",new Vector(1,2).plus(new Vector(2,3)));
console.log("Разность векторов: ", new Vector(1,2).minus(new Vector(2,3)));
