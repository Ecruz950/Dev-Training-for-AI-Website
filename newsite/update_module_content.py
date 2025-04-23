from app import create_app, db
from app.models import Module
import os

def update_module_content():
    """
    Update the title and description of Module 1
    """
    app = create_app()
    
    with app.app_context():
        # Find Module 1
        module = Module.query.filter_by(id=1).first()
        
        if module:
            print(f"Current module title: {module.title}")
            print(f"Current module description: {module.description}")
            
            # Update the module
            module.title = 'Introduction to LLMs and Responsible Use'
            module.description = 'Learn about the common misconceptions of artificial intelligence, large language models, and generative models as well as some pointers on how to utilize such software for whatever task you need.'
            
            # Save changes
            db.session.commit()
            
            print("Module updated successfully!")
            print(f"New title: {module.title}")
            print(f"New description: {module.description}")
        else:
            print("Module not found!")
            
            # Create the module if it doesn't exist
            module = Module(
                id=1,
                title='Introduction to LLMs and Responsible Use',
                description='Learn about the common misconceptions of artificial intelligence, large language models, and generative models as well as some pointers on how to utilize such software for whatever task you need.',
                video_path='modules/module1Video.mp4',
                order=1
            )
            db.session.add(module)
            db.session.commit()
            print("Module created successfully!")

if __name__ == '__main__':
    update_module_content() 