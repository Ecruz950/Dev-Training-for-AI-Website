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

## Current Modules

1. **Introduction to LLMs and Responsible Use**
   - Description: Learn about the common misconceptions of artificial intelligence, large language models, and generative models as well as some pointers on how to utilize such software for whatever task you need.
   - Video: module1Video.mp4
   - Quiz: 1_quiz.json

2. **Developer Tips for using AI**
   - Description: Learn about the common pitfalls and best practices when working with large language models
   - Video: module2Video.mp4
   - Quiz: 2_quiz.json

## Prerequisites

- Python 3.8+
- Flask and extensions
- SQLite (default) or MySQL/PostgreSQL
- Nginx (for production)
- Systemd (for production)

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
   python setup_local_db.py
   python create_quiz.py
   ```

5. Start the application:
   ```
   python wsgi.py
   ```

6. Access the application:
   Open your browser and go to `http://localhost:5000`

## Production Deployment

The application is designed to run on an EC2 instance with the following setup:

- t2.micro instance with 2GB swap space
- Nginx reverse proxy
- Systemd service for Flask app management
- PostgreSQL database

### Production Requirements

1. Environment Variables:
   - Create `.env.production` with production settings
   - Set `FLASK_ENV=production`
   - Configure database URL
   - Set secret key

2. Nginx Configuration:
   - Reverse proxy to Flask app
   - Static file handling
   - Proper caching headers
   - SSL configuration (if using HTTPS)

3. Systemd Service:
   - Automatic startup
   - Process management
   - Log rotation

4. File Permissions:
   - Proper ownership for static files
   - Secure upload directory
   - Database access rights

## Project Structure

```
newsite/
├── app/                  # Application package
│   ├── admin/            # Admin blueprint
│   ├── auth/             # Authentication blueprint
│   ├── main/             # Main blueprint
│   ├── modules/          # Modules blueprint
│   ├── static/           # Static files
│   │   ├── modules/      # Module videos
│   │   └── quizzes/      # Quiz JSON files
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
- See `deployment_guide.md` for production deployment instructions

## License

MIT

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request 