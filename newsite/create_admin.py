from app import create_app, db
from app.models import User
import os

def create_admin_user():
    app = create_app()
    with app.app_context():
        # Check if admin user already exists
        admin = User.query.filter_by(username='admin').first()
        
        if admin:
            print(f"Admin user found: {admin.username} (is_admin={admin.is_admin}, is_group_admin={admin.is_group_admin})")
            print("Updating admin permissions...")
            # Delete existing admin for a clean start
            db.session.delete(admin)
            db.session.commit()
            print("Existing admin account deleted.")
        
        # Create fresh admin user
        admin = User(
            username='admin',
            email='admin@example.com',
            is_admin=True,
            is_group_admin=True,
            is_active=True
        )
        admin.set_password('admin123')
        
        try:
            # Add to database
            db.session.add(admin)
            db.session.commit()
            
            print('Admin user created successfully!')
            print('Username: admin')
            print('Password: admin123')
            print(f'Admin permissions: is_admin={admin.is_admin}, is_group_admin={admin.is_group_admin}')
        except Exception as e:
            db.session.rollback()
            print(f'Error creating admin user: {str(e)}')
            
        # Create a module if none exists
        from app.models import Module
        if Module.query.count() == 0:
            print("Creating sample module...")
            module = Module(
                title="Introduction to Programming",
                description="Learn the basics of programming with this introductory module.",
                order=1
            )
            db.session.add(module)
            db.session.commit()
            print("Sample module created successfully!")

if __name__ == '__main__':
    create_admin_user() 