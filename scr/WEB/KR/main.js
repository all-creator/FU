let p_one = {
    isDo: false,
    c_errors: 9
};
let p_two = {
    isDo: false,
    c_errors: 9
};
let game = {
    word: "",
    ans_word: ""
};

// utils

let alf = ["А","Б","В","Г","Д","Е","Ё","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"]

function printInv(str) {
    document.getElementsByClassName("invite")[0].innerHTML = str;
}

function printLabel(str) {
    document.getElementsByClassName("label")[0].innerHTML = str;
}

function isInWord(char) {
    return game.word.search(char.toLowerCase()) !== -1
}

String.prototype.replaceAt = function(index, replacement) {
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}

// step 1

function getP() {
    return Math.round(Math.random()) === 1 ? "Играет первый игрок" : "Играет второй игрок"
}

function choosePlayer(){
    let player = getP()
    if (player.indexOf("первый")) {
        p_one.isDo = true
    } else p_two.isDo = true
    printInv(player)
}

// step 2

function getWord() {
    printLabel("Введите слово:")
}

// step 3

function setWord(str){
    game.word = str.toLowerCase()
    if (p_one.isDo) printLabel("Играет второй игрок")
    else printInv("Играет первый игрок")
    printInv("Введите букву: ")
    document.getElementById('w_st').onclick = function() {
        answer(document.getElementById('word_input').value);
        document.getElementById('w').innerHTML = game.ans_word
    };
}

// step 4

function answer(char){
    if (isInWord(char)){
        printLabel("Верно!")
        let j = game.word.indexOf(char)
        game.ans_word = game.ans_word.replaceAt(j, char)
        document.getElementById('w').innerHTML = game.ans_word
    } else {
        printLabel("Не верно!")
        p_one.c_errors--;
        document.getElementById('c_errors').value = "Осталось ошибок: " + p_one.c_errors
        document.getElementById(char).style.color = 'red';
    }
    document.getElementById('w_st').onclick = function() {
        answer(document.getElementById('word_input').value);
        document.getElementById('w').innerHTML = game.ans_word
    };
}

// full game

function startGame() {
    choosePlayer()
    getWord()
}


