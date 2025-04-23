from app import create_app, db
from app.models import User, Module, ModuleProgress

def setup_local_db():
    """Set up a local SQLite database for testing"""
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Create admin user if it doesn't exist
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@example.com',
                is_admin=True,
                is_group_admin=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Admin user created")
        else:
            print("Admin user already exists")
        
        # Create module if it doesn't exist
        module = Module.query.filter_by(id=1).first()
        if not module:
            module = Module(
                id=1,
                title='Introduction to LLMs and Responsible Use',
                description='Learn about the common misconceptions of artificial intelligence, large language models, and generative models as well as some pointers on how to utilize such software for whatever task you need.',
                video_path='modules/module1Video.mp4',
                order=1
            )
            db.session.add(module)
            db.session.commit()
            print("Module created")
        else:
            # Update module title and description
            module.title = 'Introduction to LLMs and Responsible Use'
            module.description = 'Learn about the common misconceptions of artificial intelligence, large language models, and generative models as well as some pointers on how to utilize such software for whatever task you need.'
            db.session.commit()
            print("Module updated")
        
        print("Local database setup complete!")

if __name__ == '__main__':
    setup_local_db() 