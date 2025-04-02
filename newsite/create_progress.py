from app import create_app, db
from app.models import User, Module, ModuleProgress
from datetime import datetime

app = create_app()

with app.app_context():
    # Get admin user
    admin = User.query.filter_by(username='admin').first()
    if admin:
        # Get all modules
        modules = Module.query.all()
        
        # Create progress records for admin
        for module in modules:
            # Check if progress record exists
            progress = ModuleProgress.query.filter_by(
                user_id=admin.id,
                module_id=module.id
            ).first()
            
            if not progress:
                # Create new progress record with completed status
                progress = ModuleProgress(
                    user_id=admin.id,
                    module_id=module.id,
                    video_completed=True,
                    quiz_completed=True,
                    quiz_score=100,
                    progress=100,
                    completed_at=datetime.utcnow()
                )
                db.session.add(progress)
                print(f"Created progress record for admin on Module {module.id}")
            else:
                # Update existing record to completed
                progress.video_completed = True
                progress.quiz_completed = True
                progress.quiz_score = 100
                progress.progress = 100
                if not progress.completed_at:
                    progress.completed_at = datetime.utcnow()
                print(f"Updated progress record for admin on Module {module.id}")
        
        db.session.commit()
        print("Admin progress updated successfully")
    else:
        print("Admin user not found") 