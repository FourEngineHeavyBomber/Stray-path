function fn() {
    document.getElementById('mob-nav-menu').classList.add('show-me')
    document.getElementById('mob-nav-menu').classList.remove('hide-me')
    document.getElementById('hamburger-bar').classList.add('hide-me');
}
function undo() {
    document.getElementById('mob-nav-menu').classList.remove('show-me')
    document.getElementById('mob-nav-menu').classList.add('hide-me')
    document.getElementById('hamburger-bar').classList.remove('hide-me');
    document.getElementById('hamburger-bar').classList.add('show-me');
}

function Redirect(place) {
    window.location = place;
 }