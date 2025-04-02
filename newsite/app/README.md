# Application Directory Structure

This directory contains the core application code for the AI Training Platform. It follows a blueprint-based modular architecture to organize functionality into distinct components.

## Directory Structure

```
app/
├── admin/              # Admin dashboard blueprint
│   ├── __init__.py     # Blueprint initialization
│   └── routes.py       # Admin routes and views
├── auth/               # Authentication blueprint
│   ├── __init__.py     # Blueprint initialization
│   ├── forms.py        # Authentication forms
│   └── routes.py       # Authentication routes
├── main/               # Main application blueprint
│   ├── __init__.py     # Blueprint initialization
│   └── routes.py       # Main application routes
├── modules/            # Modules and quiz blueprint
│   ├── __init__.py     # Blueprint initialization
│   └── routes.py       # Module and quiz routes
├── static/             # Static assets
│   ├── css/            # CSS stylesheets
│   ├── modules/        # Video content for modules
│   ├── quizzes/        # Quiz JSON files
│   └── uploads/        # User uploaded content
├── templates/          # HTML templates
│   ├── admin/          # Admin dashboard templates
│   ├── auth/           # Authentication templates
│   ├── main/           # Main application templates
│   ├── modules/        # Module and quiz templates
│   └── base.html       # Base template with common elements
├── __init__.py         # Application factory
└── models.py           # Database models
```

## Blueprints

The application is organized into separate blueprints:

### Admin Blueprint
- User management
- Group management 
- Progress tracking
- Platform analytics

### Auth Blueprint
- User registration
- Login/logout
- Profile management
- Password management

### Main Blueprint
- Homepage
- User profile
- Group management
- Notification handling

### Modules Blueprint
- Module listing and details
- Video content delivery
- Quiz management
- Progress tracking

## Templates

Templates are organized by blueprint with a common base template that includes:
- Navigation bar
- Sidebar
- Flash messages
- Footer

## Static Files

The static directory contains:
- CSS stylesheets for styling
- Module videos for educational content
- Quiz JSON files with questions and answers
- User uploads (profile pictures, etc.)

## Core Files

### __init__.py
- Application factory pattern
- Blueprint registration
- Extension initialization
- Configuration loading

### models.py
- SQLAlchemy ORM models
- User model with Flask-Login integration
- Relationship definitions between models

## Models

The application uses the following key models:

- **User**: User accounts with authentication and role information
- **Group**: Learning groups with members
- **GroupMember**: Association between users and groups
- **Notification**: System notifications for users
- **Module**: Learning modules with content
- **ModuleProgress**: User progress tracking for modules
- **Quiz**: Quizzes associated with modules
- **Question**: Quiz questions with options
- **Option**: Multiple choice options for questions
- **QuizAttempt**: Records of user quiz attempts

## Features

### Admin Dashboard
- User management and role assignment
- Group creation and management
- Progress monitoring and reporting
- System configuration

### Authentication System
- User registration with email verification
- Secure login with password hashing
- Profile management
- Role-based access control

### Group Management
- Create and manage learning groups
- Invite users via email
- Track group progress
- Manage group permissions

### Module System
- Video-based learning content
- Module progression tracking
- Prerequisite verification
- Completion status

### Quiz System
- Multiple-choice questions
- Immediate feedback
- Score calculation
- Results tracking

### Notification System
- User notifications
- Group invitations
- Read/unread status

## Development Notes

- Blueprint registration happens in the application factory
- Database models are defined in models.py
- Static files are configured for caching
- Templates use Jinja2 inheritance
- Flash messages provide user feedback
- Routes are protected by login_required decorators

For more detailed information on the application architecture and implementation, refer to the TECHNICAL_OVERVIEW.md file in the project root. 