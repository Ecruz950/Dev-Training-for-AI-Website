from app import create_app, db
from app.models import User

def add_active_column():
    """Add is_active column to User table if it doesn't exist"""
    app = create_app()
    
    with app.app_context():
        # Check if column exists by querying for it
        try:
            # Try to query for the column to see if it exists
            db.session.execute("SELECT is_active FROM user LIMIT 1")
            print("Column 'is_active' already exists.")
        except Exception as e:
            if "no such column" in str(e):
                print("Column 'is_active' doesn't exist. Adding it now...")
                # Add the column
                with db.engine.connect() as conn:
                    conn.execute("ALTER TABLE user ADD COLUMN is_active BOOLEAN DEFAULT 1")
                    print("Column 'is_active' added successfully!")
            else:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":
    add_active_column() 