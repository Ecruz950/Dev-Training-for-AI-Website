from app import create_app, db
from app.models import Module

def update_modules():
    """Update module 1 and add module 2"""
    app = create_app()
    
    with app.app_context():
        # Update Module 1
        module1 = Module.query.get(1)
        if module1:
            module1.title = 'Introduction to LLMs and Responsible Use'
            module1.description = 'Learn about the common misconceptions of artificial intelligence, large language models, and generative models as well as some pointers on how to utilize such software for whatever task you need.'
            module1.video_path = 'module1Video.mp4'
            print("Module 1 updated")
        else:
            module1 = Module(
                id=1,
                title='Introduction to LLMs and Responsible Use',
                description='Learn about the common misconceptions of artificial intelligence, large language models, and generative models as well as some pointers on how to utilize such software for whatever task you need.',
                video_path='module1Video.mp4',
                order=1
            )
            db.session.add(module1)
            print("Module 1 created")
        
        # Add Module 2
        module2 = Module.query.get(2)
        if not module2:
            module2 = Module(
                id=2,
                title='Developer Tips for using AI',
                description='Learn about the common pitfalls and best practices when working with large language models',
                video_path='module2Video.mp4',
                order=2
            )
            db.session.add(module2)
            print("Module 2 created")
        else:
            module2.video_path = 'module2Video.mp4'
            print("Module 2 updated")
        
        db.session.commit()
        print("Database update complete!")

if __name__ == '__main__':
    update_modules() 