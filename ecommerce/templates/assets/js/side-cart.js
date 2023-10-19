let cartSidebar = document.getElementById('cartBag')
let mobileMenu = document.getElementById('openCart1')
let closeX = document.getElementById('x')
let openSidebar = false;


cartBag.addEventListener("click", () => {
    event.preventDefault();
    openCart1.style.display = "block"; // Show the section
  });

closeX.addEventListener("click", () => {
    event.preventDefault();
    openCart1.style.display = "none"; // Hide the section
});


