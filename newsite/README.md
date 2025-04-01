# AI Training Platform

A comprehensive training platform built with Flask, designed to deliver interactive learning experiences focused on AI and development topics. The platform features a modular learning system, interactive quizzes, and an administrative dashboard for content management.

## Features

- User authentication and authorization
- Group-based access control
- Interactive learning modules
- Quiz system with multiple choice questions
- Progress tracking
- Real-time notifications
- Admin dashboard for content management
- Group management system

## Prerequisites

- Python 3.13 or higher
- PostgreSQL 17
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Dev-Training-for-AI-Website.git
cd Dev-Training-for-AI-Website/newsite
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root with the following content:
```
FLASK_APP=wsgi.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://postgres:your-password@localhost:5432/training_platform
```

5. Create the database:
```bash
# Start PostgreSQL service
# On Windows (as Administrator):
net start postgresql-x64-17
```

6. Initialize the database and create admin user:
```bash
python create_admin.py
```

## Running the Application

1. Start the Flask development server:
```bash
# On Windows:
$env:FLASK_APP = "wsgi.py"
python -m flask run

# On Unix or MacOS:
export FLASK_APP=wsgi.py
flask run
```

2. Access the application:
Open your web browser and navigate to `http://localhost:5000`

## Default Admin Account

After running `create_admin.py`, you can log in with:
- Username: admin
- Password: admin123

## Testing

1. Database Testing:
```bash
# The database will be automatically initialized when you run create_admin.py
python create_admin.py
```

2. User Interface Testing:
- Log in with the admin account
- Create a new group
- Add users to the group
- Create a module
- Create a quiz
- Test the notification system

## Project Structure

```
newsite/
├── app/
│   ├── admin/         # Admin dashboard routes and templates
│   ├── auth/          # Authentication routes and templates
│   ├── modules/       # Learning module routes and templates
│   ├── quizzes/       # Quiz system routes and templates
│   ├── static/        # Static files (CSS, JS, images)
│   ├── templates/     # Base templates
│   ├── models.py      # Database models
│   └── __init__.py    # Application factory
├── .env               # Environment variables
├── requirements.txt   # Python dependencies
├── create_admin.py    # Admin user creation script
└── wsgi.py           # Application entry point
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 