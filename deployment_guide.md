# Deployment Guide for AI Training Platform Updates

This guide outlines the changes that need to be implemented on the EC2 server for the AI Training Platform.

## Changes Overview

1. Update database schema to include is_group_admin column
2. Fix video completion tracking
3. Update group invitation logic to allow re-inviting users who previously declined
4. Update Module 1 title and description

## Implementation Steps

### 1. Update Database Schema

Create a migration script to add the missing column:

```python
# File: /home/ubuntu/Dev-Training-for-AI-Website/newsite/add_group_admin_column.py
from app import create_app, db
from app.models import User
from sqlalchemy import Column, Boolean

def add_group_admin_column():
    """Add is_group_admin column to User table if it doesn't exist"""
    app = create_app()
    
    with app.app_context():
        # Check if column exists by querying for it
        try:
            # Try to query for the column to see if it exists
            User.query.filter(User.is_group_admin == True).first()
            print("Column 'is_group_admin' already exists.")
        except Exception as e:
            if "no such column" in str(e):
                print("Column 'is_group_admin' doesn't exist. Adding it now...")
                # Add the column
                with db.engine.connect() as conn:
                    conn.execute("ALTER TABLE user ADD COLUMN is_group_admin BOOLEAN DEFAULT 0")
                    print("Column 'is_group_admin' added successfully!")
            else:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":
    add_group_admin_column()
```

### 2. Update Video Completion Tracking

Edit the file: `/home/ubuntu/Dev-Training-for-AI-Website/newsite/app/modules/routes.py`

```python
@bp.route('/<int:module_id>/video')
@login_required
def video(module_id):
    module = Module.query.get_or_404(module_id)
    
    # Set the video path if not already set
    if not module.video_path and module.id == 1:
        module.video_path = 'module1Video.mp4'
        db.session.commit()
    
    # Mark video as completed when user views it
    progress = ModuleProgress.query.filter_by(
        user_id=current_user.id,
        module_id=module_id
    ).first()
    
    if not progress:
        progress = ModuleProgress(
            user_id=current_user.id,
            module_id=module_id,
            video_completed=True
        )
        db.session.add(progress)
    else:
        progress.video_completed = True
    
    db.session.commit()
        
    return render_template('modules/video.html', module=module)
```

### 3. Update Group Invitation Logic

Edit the file: `/home/ubuntu/Dev-Training-for-AI-Website/newsite/app/main/routes.py`

In the `invite_to_group` route, modify the check for existing invitations to only consider unread (pending) invitations:

```python
# Check for existing invitation
existing_notification = Notification.query.filter(
    Notification.user_id == user.id,
    Notification.type == 'group_invite',
    Notification.read == False  # Only check for unread (pending) invitations
).first()

# Only check data field if notification exists
if existing_notification and existing_notification.data and 'group_id' in existing_notification.data:
    if int(existing_notification.data['group_id']) == group_id:
        flash('User already has a pending invitation.', 'error')
        return redirect(url_for('main.group_management'))
```

### 4. Update Module 1 Title and Description

Create a new file: `/home/ubuntu/Dev-Training-for-AI-Website/newsite/update_module_content.py`

```python
from app import create_app, db
from app.models import Module

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
                video_path='module1Video.mp4',
                order=1
            )
            db.session.add(module)
            db.session.commit()
            print("Module created successfully!")

if __name__ == '__main__':
    update_module_content()
```

## Deployment Commands

Connect to the EC2 instance and run the following commands:

```bash
# Connect to your EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-instance-ip

# Navigate to the project directory
cd Dev-Training-for-AI-Website/newsite

# Create a backup of the database
cp instance/app.db instance/app.db.backup

# Create the migration script
nano add_group_admin_column.py

# Run the migration script to add the missing column
python add_group_admin_column.py

# Create a backup of the files you're about to modify
cp app/modules/routes.py app/modules/routes.py.bak
cp app/main/routes.py app/main/routes.py.bak

# Edit the files using a text editor like nano or vim
# For example:
nano app/modules/routes.py
nano app/main/routes.py

# Create the update script
nano update_module_content.py

# Run the update script to update Module 1
python update_module_content.py

# Run the create_admin script to ensure admin user exists with correct permissions
python create_admin.py

# Restart the Gunicorn service to apply changes
sudo systemctl restart gunicorn
```

## Verification Steps

After deploying the changes, verify that:

1. You can log in with the admin user
2. Video completion is properly tracked when a user views a module video
3. Group invitations can be sent to users who previously declined them
4. Module 1 title and description are updated correctly 