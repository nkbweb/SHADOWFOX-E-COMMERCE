document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Quantity increment/decrement on product page
    if (document.getElementById('quantity-input')) {
        setupQuantityButtons();
    }

    // Setup add to cart form submission
    if (document.getElementById('add-to-cart-form')) {
        setupAddToCartForm();
    }

    // Setup remove from cart buttons
    setupRemoveFromCartButtons();
});

function setupQuantityButtons() {
    const quantityInput = document.getElementById('quantity-input');
    const incrementBtn = document.getElementById('increment-btn');
    const decrementBtn = document.getElementById('decrement-btn');

    if (incrementBtn && decrementBtn && quantityInput) {
        incrementBtn.addEventListener('click', function() {
            let currentValue = parseInt(quantityInput.value, 10);
            if (!isNaN(currentValue)) {
                quantityInput.value = currentValue + 1;
            }
        });

        decrementBtn.addEventListener('click', function() {
            let currentValue = parseInt(quantityInput.value, 10);
            if (!isNaN(currentValue) && currentValue > 1) {
                quantityInput.value = currentValue - 1;
            }
        });
    }
}

function setupAddToCartForm() {
    const form = document.getElementById('add-to-cart-form');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const productId = form.getAttribute('data-product-id');
        const quantity = document.getElementById('quantity-input').value;
        
        fetch('/cart/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({
                product_id: productId,
                quantity: quantity
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showToast('Product added to cart!', 'success');
                updateCartCount(data.cart_count);
            } else {
                showToast(data.message || 'Failed to add product to cart.', 'danger');
            }
        })
        .catch(error => {
            console.error('Error adding to cart:', error);
            showToast('An error occurred. Please try again.', 'danger');
        });
    });
}

function setupRemoveFromCartButtons() {
    const removeButtons = document.querySelectorAll('.remove-from-cart');
    removeButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.getAttribute('data-product-id');
            
            fetch(`/cart/remove/${productId}`, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const cartItem = this.closest('.cart-item');
                    if (cartItem) {
                        cartItem.remove();
                    }
                    updateCartTotal(data.cart_total);
                    updateCartCount(data.cart_count);
                    
                    if (data.cart_count === 0) {
                        document.querySelector('.cart-items').innerHTML = '<p class="text-center my-5">Your cart is empty</p>';
                        document.querySelector('.cart-summary').style.display = 'none';
                    }
                    
                    showToast('Product removed from cart!', 'success');
                } else {
                    showToast(data.message || 'Failed to remove product from cart.', 'danger');
                }
            })
            .catch(error => {
                console.error('Error removing from cart:', error);
                showToast('An error occurred. Please try again.', 'danger');
            });
        });
    });
}

function updateCartCount(count) {
    const cartCountElem = document.getElementById('cart-count');
    if (cartCountElem) {
        cartCountElem.textContent = count;
    }
}

function updateCartTotal(total) {
    const cartTotalElem = document.getElementById('cart-total');
    if (cartTotalElem) {
        cartTotalElem.textContent = '$' + parseFloat(total).toFixed(2);
    }
}

function showToast(message, type) {
    const toastContainer = document.getElementById('toast-container');
    
    if (!toastContainer) {
        const newContainer = document.createElement('div');
        newContainer.id = 'toast-container';
        newContainer.className = 'position-fixed bottom-0 end-0 p-3';
        document.body.appendChild(newContainer);
    }
    
    const toastId = 'toast-' + Date.now();
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    toast.id = toastId;
    
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;
    
    document.getElementById('toast-container').appendChild(toast);
    
    const bsToast = new bootstrap.Toast(toast, {
        animation: true,
        autohide: true,
        delay: 3000
    });
    
    bsToast.show();
    
    toast.addEventListener('hidden.bs.toast', function() {
        toast.remove();
    });
} 