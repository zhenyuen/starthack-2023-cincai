const chat_messages = document.getElementsByClassName("chat-container");

for (let i = 0; len = chat_messages.length, i < len; i++) {
    var current = chat_messages[i]; // replace "myDiv" with the ID of your div
    var value = Number(chat_messages[i].lastElementChild.innerHTML)
    value = (value + 2) / 0.9
    var r = 255 - (value - 1) * 25.5; // decrease red value as value increases
    var g = (value - 1) * 25.5; // increase green value as value increases
    var b = 0; // set blue value to 0
    current.style.backgroundColor = "rgb(" + r + "," + g + "," + b + ")";
}