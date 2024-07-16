async function addToCart() {
    const productId = document.getElementById('cart_product_id').value;
    const name = document.getElementById('cart_name').value;
    const price = document.getElementById('cart_price').value;
    const imageUrl = document.getElementById('cart_image_url').value;

    const response = await fetch('/cart/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            product_id: productId,
            name: name,
            price: price,
            image_url: imageUrl
        })
    });

    const result = await response.json();
    alert(result.message);
}

async function addToCart() {
    const productId = document.getElementById('cart_product_id').value;
    const name = document.getElementById('cart_name').value;
    const price = parseFloat(document.getElementById('cart_price').value);  // Ensure price is parsed as float
    const imageUrl = document.getElementById('cart_image_url').value;

    const response = await fetch('/cart/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            product_id: productId,
            name: name,
            price: price,
            image_url: imageUrl
            })
    });
}

async function addToWishlist() {
    const productId = document.getElementById('wishlist_product_id').value;
    const name = document.getElementById('wishlist_name').value;
    const price = document.getElementById('wishlist_price').value;
    const imageUrl = document.getElementById('wishlist_image_url').value;

    const response = await fetch('/wishlist/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            product_id: productId,
            name: name,
            price: price,
            image_url: imageUrl
        })
    });

    const result = await response.json();
    alert(result.message);
}

async function getCartItems() {
    const response = await fetch('/cart/items');
    const items = await response.json();

    const cartItems = document.getElementById('cart_items');
    cartItems.innerHTML = '';

    items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - $${item.price}`;
        cartItems.appendChild(li);
    });
}

async function getWishlistItems() {
    const response = await fetch('/wishlist/items');
    const items = await response.json();

    const wishlistItems = document.getElementById('wishlist_items');
    wishlistItems.innerHTML = '';

    items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - $${item.price}`;
        wishlistItems.appendChild(li);
    });
}
