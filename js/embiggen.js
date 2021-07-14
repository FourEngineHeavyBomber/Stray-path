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