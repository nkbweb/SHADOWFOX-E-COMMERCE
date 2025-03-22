# Multi-Vendor Marketplace

A Flask-based e-commerce platform that supports multiple shop owners selling products on a single marketplace.

## Features

- **Multi-vendor support**: Different shop owners can manage their own products
- **Product management**: Add, edit, delete, and claim products
- **Order management**: Track and update order status
- **User authentication**: Separate flows for customers and shop owners
- **Shopping cart**: Add products to cart and checkout
- **Responsive design**: Works on desktop and mobile devices

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/marketplace.git
   cd marketplace
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the application:
   ```
   FLASK_APP=app FLASK_DEBUG=1 flask run
   ```

6. Visit `http://localhost:5000` in your browser

## Shop Owner Features

- Dashboard with stats specific to their products
- Ability to claim unclaimed products
- Order management for orders containing their products
- Product inventory management

## Customer Features

- Browse products from multiple vendors
- Add products to cart
- Checkout process
- Order history

## Technologies Used

- Flask
- SQLAlchemy
- Bootstrap 5
- JavaScript
- SQLite (can be configured for other databases)

## License

[MIT License](LICENSE) 