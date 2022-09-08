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
    ans_word: "",
    player: NaN
};

// utils

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
        game.player = 1
    } else {
        p_two.isDo = true
        game.player = 2
    }
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
        let str = game.word
        for (let j = 0; j < str.length; j++) {
            if (game.word.charAt(j) === char){
                game.ans_word = game.ans_word.replaceAt(j, char)
            }
        }
        document.getElementById('w').innerHTML = game.ans_word
        document.getElementById(char).style.color = 'green';
        if (game.word === game.ans_word) {
            printInv("Вы выиграли")
            printLabel("Загаданное слово: " + game.word)
        }
    } else {
        printLabel("Не верно!")
        p_one.c_errors--;
        document.getElementById('c_errors').innerHTML = "Осталось ошибок: " + p_one.c_errors
        document.getElementById(char).style.color = 'red';
        if (p_two.c_errors === 0 || p_one.c_errors === 0) {
            printInv("Вы проиграли")
            printLabel("Загаданное слово: " + game.word)
        }
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


