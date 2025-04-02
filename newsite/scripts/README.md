# Utility Scripts

This directory contains utility scripts for managing and maintaining the AI Training Platform. These scripts help with database initialization, content management, and maintenance tasks.

## Available Scripts

### User Management
- **create_admin.py** - Creates an admin user with default credentials (admin/admin123) or updates an existing admin user with proper permissions.

### Content Management
- **import_modules.py** - Imports module data into the database from predefined configurations.
- **create_quiz.py** - Creates a quiz record in the database for Module 1 with the appropriate settings.
- **create_quiz_questions.py** - Imports questions from the JSON file (app/static/quizzes/1_quiz.json) into the database Quiz model.
- **update_quiz.py** - Updates quiz properties such as passing score.

### Data Maintenance
- **check_module_data.py** - Validates and fixes module video paths in the database.
- **create_progress.py** - Updates or creates progress records for users, particularly for ensuring admin has proper progress records.

## Usage Instructions

### Initial Setup
When setting up the application for the first time, run the scripts in this order:

1. **create_admin.py** - Sets up the admin user
   ```bash
   python create_admin.py
   ```

2. **import_modules.py** - Imports module data
   ```bash
   python import_modules.py
   ```

3. **create_quiz.py** - Creates the Module 1 quiz
   ```bash
   python create_quiz.py
   ```

4. **create_quiz_questions.py** - Imports the quiz questions
   ```bash
   python create_quiz_questions.py
   ```

### Maintenance Tasks
For maintenance or troubleshooting:

1. **check_module_data.py** - Fixes video paths
   ```bash
   python check_module_data.py
   ```

2. **create_progress.py** - Updates progress records
   ```bash
   python create_progress.py
   ```

3. **update_quiz.py** - Updates quiz properties
   ```bash
   python update_quiz.py
   ```

## Development Notes

- All scripts use the application context to access models and the database
- Scripts are designed to be idempotent (safe to run multiple times)
- Error handling is implemented to prevent duplicate records
- Debug output is provided to verify operations

## Adding New Scripts

When adding new scripts, follow these guidelines:

1. Use the application factory pattern:
   ```python
   from app import create_app, db
   # Import required models
   
   app = create_app()
   
   with app.app_context():
       # Script logic here
   ```

2. Include proper error handling and verbose output
3. Make scripts idempotent when possible
4. Include descriptive comments
5. Update this README when adding new scripts 