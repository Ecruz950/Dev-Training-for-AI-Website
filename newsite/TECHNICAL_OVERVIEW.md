# Technical Overview: AI Training Website

## Project Overview
This is a comprehensive training platform built with Flask, designed to deliver interactive learning experiences focused on AI and development topics. The platform features a modular learning system, interactive quizzes, and an administrative dashboard for content management.

## Technical Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLAlchemy with PostgreSQL
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Frontend**: Bootstrap 5, Custom CSS/JavaScript
- **Template Engine**: Jinja2
- **Media Handling**: Flask's send_from_directory for video content
- **Production Server**: Nginx with systemd service management
- **Hosting**: AWS EC2 t2.micro instance with 2GB swap space

## Core Features

### 1. User Management System
- **Authentication**
  - User registration with email verification
  - Secure login system with "Remember Me" functionality
  - Password reset functionality
  - Session management
- **User Roles**
  - Admin users with full system access
  - Group admin users with group management capabilities
  - Regular users with learning access
  - Role-based UI elements
- **Group Management**
  - Group creation and management
  - Email-based group invitations
  - Group member management
  - Group-based progress tracking
  - Group admin role with limited administrative privileges

### 2. Learning Management System
- **Module Structure**
  - Video-based learning content
  - Progress tracking per module
  - Completion status monitoring
  - Visual progress indicators
- **Current Modules**
  1. **Introduction to LLMs and Responsible Use**
     - Video content on AI misconceptions and usage
     - Interactive quiz with detailed feedback
     - Progress tracking for video and quiz completion
  2. **Developer Tips for using AI**
     - Video content on development best practices
     - Interactive quiz with detailed feedback
     - Progress tracking for video and quiz completion
- **Content Types**
  - Video content (MP4)
  - Interactive quizzes
  - Text-based content
  - Visual feedback systems

### 3. Quiz System
- **Quiz Features**
  - Multiple choice questions with immediate feedback
  - Real-time correct/incorrect indicators
  - Interactive completion system
  - Detailed explanations for both correct and incorrect answers
  - Progress tracking with visual indicators
- **Quiz Management**
  - JSON-based question data
  - Question importing system
  - Database persistence for quiz attempts
  - 100% completion requirement
- **Current Quizzes**
  1. Module 1 Quiz: Introduction to LLMs
  2. Module 2 Quiz: Developer Tips

### 4. Admin Dashboard
- **Content Management**
  - Module creation and editing
  - Module progress tracking across users
  - Quiz management
  - Question and answer management
- **User Management**
  - User role assignment
  - User progress monitoring
  - Group management
  - Detailed progress visualization

### 5. Progress Tracking
- **User Progress**
  - Module completion status
  - Quiz completion status
  - Visual progress indicators
  - Admin monitoring capabilities
- **Analytics**
  - User engagement metrics
  - Module completion rates
  - Group-based progress tracking

### 6. Notification System
- **In-App Notifications**
  - Group invitations
  - Acceptance/rejection functionality
  - Notification counter in navigation
  - Notification management
- **Notification Management**
  - Mark as read/unread functionality
  - Accept/reject interface for invitations
  - Notification history

## Technical Implementation Details

### Database Schema
- **User Model**
  - Authentication fields (username, email, password_hash)
  - Role management fields (is_admin, is_group_admin)
  - Relationship to groups and notifications
  - Preferences fields
- **Group Model**
  - Group information (name, description)
  - Member relationships (many-to-many with users)
  - Admin relationship (one-to-many with users)
  - Creation timestamp
- **Module Model**
  - Content structure (title, description)
  - Video path for media content
  - Order field for sequencing
  - Relationship to progress records
- **Quiz Model**
  - Relationship to module (one-to-one)
  - Questions relationship (one-to-many)
  - Passing score configuration
  - Relationship to attempts
- **ModuleProgress Model**
  - User and module relationships
  - Video completion tracking
  - Quiz completion tracking
  - Timestamp fields for tracking
- **Question Model**
  - Relationship to quiz
  - Question text and order
  - Options relationship (one-to-many)
- **Option Model**
  - Relationship to question
  - Text content and correctness flag
  - Order field for display sequence
- **Notification Model**
  - User relationship (target user)
  - Type field for notification categorization
  - Content field for notification text
  - Data field (JSON) for additional information
  - Read status tracking

### Security Features
- Password hashing with Werkzeug
- CSRF protection with Flask-WTF
- Session management with Flask-Login
- Role-based access control
- Group-based permissions
- Route protection with decorators
- Production environment configuration
- Secure file permissions
- Nginx security headers

### Frontend Implementation
- **Responsive Design**
  - Mobile-first approach
  - Sidebar navigation with hover effect
  - Custom CSS for enhanced UI
  - Consistent color scheme and styling
- **Interactive Features**
  - Real-time quiz feedback
  - Dynamic progress indicators
  - Interactive completion system
  - Flash message system
- **User Experience**
  - Intuitive navigation
  - Clear visual feedback
  - Consistent styling across pages
  - Animated transitions

### Media Handling
- Video content served through Flask routes
- Static file organization for media content
- Video playback with HTML5 video elements
- Proper MIME type handling
- Nginx static file serving
- Caching headers for static content

## Production Deployment

### Server Configuration
- AWS EC2 t2.micro instance
- 2GB swap space for memory management
- Nginx reverse proxy configuration
- Systemd service management
- PostgreSQL database
- Environment-specific settings

### Performance Optimization
- Static file caching
- Nginx gzip compression
- Database connection pooling
- Memory management
- Swap space utilization

### Security Measures
- Production environment variables
- Secure file permissions
- Nginx security headers
- Database access controls
- Regular backups

## Development Tools and Scripts

### Utility Scripts
- `setup_local_db.py` - Initializes database and creates admin user
- `create_quiz.py` - Sets up quiz records in the database
- `update_modules.py` - Updates module content and paths
- `create_progress.py` - Manages progress records
- `check_module_data.py` - Validates and fixes module paths
- `update_quiz.py` - Updates quiz configuration

### Code Organization
```
newsite/
├── app/
│   ├── admin/         # Admin routes and templates
│   ├── auth/          # Authentication routes and templates
│   ├── main/          # Main application routes
│   ├── modules/       # Module routes and templates
│   ├── static/        # Static files
│   │   ├── css/       # Stylesheets
│   │   ├── modules/   # Module videos
│   │   └── quizzes/   # Quiz JSON data
│   ├── templates/     # HTML templates
│   │   ├── admin/     # Admin templates
│   │   ├── auth/      # Auth templates
│   │   ├── main/      # Main app templates
│   │   └── modules/   # Module templates
│   ├── models.py      # Database models
│   └── __init__.py    # Application factory
├── scripts/           # Utility scripts
├── instance/          # Instance-specific files
├── config.py          # Configuration settings
└── wsgi.py            # Application entry point
```

## Recent Updates
- Added Module 2: Developer Tips for using AI
- Updated Module 1 content and description
- Improved video path handling
- Enhanced quiz system with better feedback
- Optimized production deployment
- Added comprehensive documentation

## Development Guidelines

### Code Organization
```
training_website/
├── app/
│   ├── models/         # Database models
│   ├── routes/         # Route handlers
│   ├── forms/          # Form definitions
│   ├── templates/      # HTML templates
│   ├── static/         # Static files
│   └── utils/          # Utility functions
├── config.py           # Configuration settings
├── requirements.txt    # Dependencies
└── run.py             # Application entry point
```

### Best Practices
- Follow PEP 8 style guide
- Use type hints for better code clarity
- Implement proper error handling
- Write comprehensive docstrings
- Maintain consistent code formatting
- Use meaningful variable names
- Implement proper logging

### Testing Strategy
- Unit tests for models and utilities
- Integration tests for routes
- Form validation tests
- Security testing
- User acceptance testing

## Deployment Considerations
- Environment variable management
- Database migrations
- Static file serving
- Email server configuration
- Security headers
- Error logging
- Performance optimization

## Future Enhancements
- Real-time collaboration features
- Advanced analytics dashboard
- API integration capabilities
- Mobile application
- Gamification elements
- Social learning features
- Content recommendation system

## Support and Maintenance
- Regular security updates
- Performance monitoring
- Backup procedures
- User support system
- Documentation updates
- Bug tracking and resolution

This technical overview provides a comprehensive understanding of the system's architecture, features, and implementation details. For specific implementation details, refer to the individual component documentation and code comments. 

### Recent Changes
- Removed email sending functionality in favor of in-app notifications
- Implemented comprehensive group management system
- Added real-time notification system
- Updated database schema to support groups and notifications
- Enhanced user interface for group management
- Added notification preferences and management 