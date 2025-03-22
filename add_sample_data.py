from app import create_app, db
from app.models import Product, User
import random

def add_sample_data():
    app = create_app()
    with app.app_context():
        # Create admin user if it doesn't exist
        admin = User.query.filter_by(email='admin@example.com').first()
        if not admin:
            admin = User(username='admin', email='admin@example.com', is_admin=True)
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print('Admin user created!')
        
        # Create sample products
        products = [
            {
                'name': 'Smartphone X',
                'description': 'Latest smartphone with advanced features and a stunning display.',
                'price': 799.99,
                'stock': 50,
                'category': 'Electronics',
                'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80'
            },
            {
                'name': 'Laptop Pro',
                'description': 'Powerful laptop for professional work and gaming with high performance.',
                'price': 1299.99,
                'stock': 30,
                'category': 'Electronics',
                'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80'
            },
            {
                'name': 'Wireless Headphones',
                'description': 'Premium noise-cancelling headphones with long battery life.',
                'price': 199.99,
                'stock': 100,
                'category': 'Electronics',
                'image_url': 'https://images.unsplash.com/photo-1613040809024-b4ef7ba99bc3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80'
            },
            {
                'name': 'Smart Watch',
                'description': 'Fitness tracker and smartwatch with heart rate monitoring and GPS.',
                'price': 249.99,
                'stock': 75,
                'category': 'Electronics',
                'image_url': 'https://images.unsplash.com/photo-1579586337278-3befd40fd17a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80'
            },
            {
                'name': 'Casual T-Shirt',
                'description': 'Comfortable cotton t-shirt for everyday wear.',
                'price': 24.99,
                'stock': 200,
                'category': 'Clothing',
                'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80'
            },
            {
                'name': 'Designer Jeans',
                'description': 'Premium quality denim jeans with perfect fit.',
                'price': 89.99,
                'stock': 150,
                'category': 'Clothing',
                'image_url': 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80'
            },
            {
                'name': 'Running Shoes',
                'description': 'Lightweight and comfortable shoes for running and exercise.',
                'price': 129.99,
                'stock': 80,
                'category': 'Footwear',
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80'
            },
            {
                'name': 'Coffee Maker',
                'description': 'Automatic coffee maker with timer and multiple brewing options.',
                'price': 79.99,
                'stock': 40,
                'category': 'Home & Kitchen',
                'image_url': 'https://images.unsplash.com/photo-1517488629431-6427e0ee1e5f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80'
            },
            {
                'name': 'Blender',
                'description': 'High-powered blender for smoothies and food processing.',
                'price': 69.99,
                'stock': 60,
                'category': 'Home & Kitchen',
                'image_url': 'https://images.unsplash.com/photo-1612878010854-a5954d79bfc0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80'
            },
            {
                'name': 'Yoga Mat',
                'description': 'Non-slip yoga mat for home workouts and yoga practice.',
                'price': 29.99,
                'stock': 120,
                'category': 'Sports & Fitness',
                'image_url': 'https://images.unsplash.com/photo-1518611012118-696072aa579a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80'
            }
        ]
        
        # Add products if they don't exist
        for product_data in products:
            product = Product.query.filter_by(name=product_data['name']).first()
            if not product:
                product = Product(**product_data)
                db.session.add(product)
        
        db.session.commit()
        print(f'{len(products)} sample products added!')

if __name__ == '__main__':
    add_sample_data() 