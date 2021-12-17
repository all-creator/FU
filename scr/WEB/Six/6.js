obj = {
    method_one: function () {
        return this;
    },
    method_two: function () {
        return this;
    },
    method_th: function () {
        return "method3";
    }
};

console.log(obj.method_one().method_two().method_th());