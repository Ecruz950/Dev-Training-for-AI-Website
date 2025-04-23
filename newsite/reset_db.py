from app import create_app, db
import os

def reset_database():
    """Drop all tables and recreate them"""
    app = create_app()
    
    with app.app_context():
        print("Dropping all tables...")
        db.drop_all()
        print("Tables dropped successfully.")
        
        print("Creating all tables...")
        db.create_all()
        print("Tables created successfully.")
        
        print("Database reset complete!")

if __name__ == '__main__':
    # Ask for confirmation
    confirm = input("This will delete all data in the database. Are you sure? (y/n): ")
    if confirm.lower() == 'y':
        reset_database()
    else:
        print("Database reset cancelled.") 