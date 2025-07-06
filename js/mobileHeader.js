// Function to toggle the mobile header (hamburger menu)
function toggleMenu() {
    const hamburger = document.querySelector('.hamburger');
    const menu = document.getElementById('mobileMenu');
    hamburger.classList.toggle('open');
    menu.classList.toggle('open');
}

