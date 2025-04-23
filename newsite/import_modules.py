from app import create_app, db
from app.models import Module
import os
import shutil

def import_modules():
    app = create_app()
    with app.app_context():
        # Create modules directory if it doesn't exist
        modules_dir = os.path.join(app.static_folder, 'modules')
        os.makedirs(modules_dir, exist_ok=True)
        
        # Copy module files from old site
        old_site_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'site')
        old_modules_dir = os.path.join(old_site_dir, 'modules')
        
        # Copy module1 video
        shutil.copy2(
            os.path.join(old_modules_dir, 'module1Video.mp4'),
            os.path.join(modules_dir, 'module1Video.mp4')
        )
        
        # Create Module 1 in database
        module1 = Module(
            title='Introduction to AI',
            description='Learn the basics of artificial intelligence and its applications.',
            video_path='modules/module1Video.mp4',
            order=1
        )
        
        try:
            db.session.add(module1)
            db.session.commit()
            print('Module 1 imported successfully!')
        except Exception as e:
            db.session.rollback()
            print(f'Error importing Module 1: {str(e)}')

if __name__ == '__main__':
    import_modules() 