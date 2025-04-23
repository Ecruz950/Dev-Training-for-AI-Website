from app import create_app, db
from app.models import Module

app = create_app()

with app.app_context():
    module = Module.query.filter_by(id=1).first()
    if module:
        print(f"Module 1 video path: '{module.video_path}'")
        
        # Fix the path if needed
        if module.video_path and 'modules/' in module.video_path:
            # Remove the duplicate modules/ prefix
            module.video_path = module.video_path.replace('modules/', '')
            db.session.commit()
            print(f"Fixed module 1 video path: '{module.video_path}'")
    else:
        print("Module 1 not found") 