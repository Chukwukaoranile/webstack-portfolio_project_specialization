let productCard = document.querySelector(".productCard-container");
console.log(productCard);

let generateProducts = () => {
  return (productCard.innerHTML = products.map((x) => {
    let { id, name, type, price, image } = x;
    return `
    <section id=product-id-${id} class="productCard">
<div>
<a id=${id} href="" class="anchor-card">
  <div class="product-img_container">
    <img src=${image} alt="" />
    <a href="">
      <i class="fa-solid fa-cart-shopping card-cart"></i>
    </a>
  </div>
</a>

<div>
  <p class="product-name">${name}</p>
  <p class="product-type">${type}</p>
  <div class="rating">
    <i class="fa-regular fa-star"></i>
    <i class="fa-regular fa-star"></i>
    <i class="fa-regular fa-star"></i>
    <i class="fa-regular fa-star"></i>
    <i class="fa-regular fa-star"></i>
  </div>
  <p class="price">$ ${price}</p>
  <a href="/ecommerce/templates/assets/1.html" class="product-link" data-image="${image}">Go to Page 2</a>
</div>
</div>
</section>;
    `;
  }));
};

generateProducts();
