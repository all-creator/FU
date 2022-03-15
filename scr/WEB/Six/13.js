console.log("13\n");

function TextCell(text){
    this.text = text;
}

function StretchCell(inner, width, height){
    this.text = inner.text;
    this.width = width;
    this.height = height;

    this.minWidth = function () {
        return Math.max(
            this.text.split('\n').sort(
                function(a,b){
                    return b.length - a.length})[0]
                .length,
            this.width)
    }

    this.minHeight = function () {
        return Math.max(this.text.split('\n').length, this.height)
    }

    this.draw = function(width_in, height_in){
        let text_joined = this.text.split('\n').join('');
        text_joined += " ".repeat(width_in*height_in - text_joined.length);
        let cell = [];
        for (let i=0; i<height_in; i++){
            let s = '';
            for (let j=0; j<width_in; j++){
                s += text_joined[i*width_in + j];
            }
            cell.push(s);
        }
        return cell;
    }
}

let sc = new StretchCell(new TextCell("ab\nde\nevf"), 1, 2);
console.log("Min width: ", sc.minWidth());
console.log("Min height: " ,sc.minHeight());
console.log("Draw: ", sc.draw(5,3));