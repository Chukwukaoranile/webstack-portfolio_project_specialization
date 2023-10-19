let cartSidebar = document.getElementById('cartBag')
let mobileMenu = document.getElementById('openCart1')
let closeX = document.getElementById('x')



cartBag.addEventListener("click", () => {
    event.preventDefault();
    openCart1.style.display = "block"; // Show the section
  });

closeX.addEventListener("click", () => {
    event.preventDefault();
    openCart1.style.display = "none"; // Hide the section
});

let navSidebar = document.getElementById('navOpen')
let sideNav = document.getElementById('nav-sidebar')
let closeNav = document.getElementById('nav-x')

navOpen.addEventListener("click", () => {
    event.preventDefault();
    sideNav.style.display = "block"; // Show the section
  });

closeNav.addEventListener("click", () => {
    event.preventDefault();
    sideNav.style.display = "none"; // Hide the section
});
