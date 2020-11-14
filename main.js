let titles = [
    "Hello There",
    "Generel Kenobi",
    "Wassup",
    "Konichuaaaaaaaa"
];

function random_title() {
    let index = Math.floor((Math.random() * titles.length));
    return titles[index];
}

let header = document.getElementById("title");
header.innerText = random_title();
