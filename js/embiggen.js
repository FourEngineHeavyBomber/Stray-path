function embiggen(element) {
    document.getElementById('modal-container').style.display = 'block';
    document.getElementById('modal-img').src = element.src;
}
function unembiggen() {
    document.getElementById('modal-container').style.display = 'none';
}

document.addEventListener('keydown', (event) => {
    switch (event.keyCode) {
        // close the modal
        case 27:
            unembiggen();
    }
});

function embiggener(element) {
    var myPath = element.src;
    var ftIndex = myPath.indexOf("small");
    var sdIndex = myPath.lastIndexOf("/");
    result = myPath.substring(0, ftIndex) + 'stills' + myPath.substring(sdIndex);
    document.getElementById('modal-container').style.display = 'block';
    document.getElementById('modal-img').src = result;
}