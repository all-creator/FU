console.log("14\n");

let Iterator = {
    nextIndex: 0,

    next: function(array) {
        return this.nextIndex < array.length ?
            {value: array[this.nextIndex++], done: false} :
            {done: true};
    }
}

function ArraySeq(array) {
    Iterator.nextIndex = 0
    return {
        next: function() {
            return Iterator.next(array)
        }
    }
}

function can(obj, methodName) {
    return ((typeof obj[methodName]) == "function");
}

function logFive(obj) {
    for (let i = 0; i < 5; i++) {
        if(!can(obj, 'next')) {throw "Object should implement Iterator"}
        let nx = obj.next()
        if (nx.done) return;
        console.log(nx.value)
    }
}

function RangeSeq(from, to) {
    Iterator.nextIndex = 0
    return {
        next: function() {
            return Iterator.next(Array.apply(null, {length: to+1}).map(Number.call, Number).slice(from))
        }
    }
}

logFive(new ArraySeq([1,2]))

logFive(new RangeSeq(100,1000))
