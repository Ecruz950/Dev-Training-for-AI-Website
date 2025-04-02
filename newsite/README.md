# AI Training Platform

A comprehensive web-based platform for AI training, featuring modules, quizzes, and group-based learning.

## Features

- **Authentication System**: User registration, login, profile management
- **Admin Dashboard**: User management, group creation, and progress tracking
- **Group Management**: Create groups, add members, and manage group admins
- **Module System**: Educational modules with video content and detailed descriptions
- **Quiz System**: Interactive quizzes with multiple-choice questions and detailed feedback
- **Progress Tracking**: Track module completion and quiz performance
- **Responsive Design**: Mobile-friendly interface

## Prerequisites

- Python 3.8+
- Flask and extensions
- SQLite (default) or MySQL/PostgreSQL

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-training-platform.git
   cd ai-training-platform
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   cd newsite
   python scripts/create_admin.py
   python scripts/import_modules.py
   python scripts/create_quiz.py
   python scripts/create_quiz_questions.py
   ```

5. Start the application:
   ```
   python wsgi.py
   ```

6. Access the application:
   Open your browser and go to `http://localhost:5000`

## Project Structure

```
newsite/
├── app/                  # Application package
│   ├── admin/            # Admin blueprint
│   ├── auth/             # Authentication blueprint
│   ├── main/             # Main blueprint
│   ├── modules/          # Modules blueprint
│   ├── static/           # Static files
│   ├── templates/        # Templates
│   ├── models.py         # Database models
│   └── __init__.py       # App factory
├── scripts/              # Utility scripts
├── instance/             # Instance-specific files
│   └── app.db            # SQLite database
├── TECHNICAL_OVERVIEW.md # Technical documentation
└── wsgi.py               # WSGI entry point
```

## Default Accounts

- Admin: `admin` / `admin123`

## Development

To run the application in development mode:

```
cd newsite
python wsgi.py
```

## Testing

Run tests using pytest:

```
pytest
```

## Documentation

- See `TECHNICAL_OVERVIEW.md` for detailed technical documentation
- See `app/README.md` for application directory structure
- See `scripts/README.md` for utility scripts documentation

## License

MIT

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request 