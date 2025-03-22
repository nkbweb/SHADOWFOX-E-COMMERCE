from app import create_app
from app.models.product import Product
from app.models.user import User

app = create_app()

with app.app_context():
    print("\nProducts and their sellers:")
    products = Product.query.all()
    
    for p in products:
        seller = User.query.get(p.seller_id) if p.seller_id else None
        seller_name = seller.username if seller else "No seller (default)"
        print(f"ID: {p.id}, Name: {p.name}, Seller ID: {p.seller_id}, Seller: {seller_name}")
    
    print("\nUsers:")
    users = User.query.all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Is Admin: {user.is_admin}") 