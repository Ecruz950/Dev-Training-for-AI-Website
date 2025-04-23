# Authentication Blueprint

This directory contains the Authentication blueprint which manages user authentication, registration, and profile management for the AI Training Platform.

## Overview

The Auth blueprint handles:
- User registration
- Login and logout
- Password management
- User profile updates
- Notification handling

## Files

- **__init__.py** - Blueprint initialization
- **routes.py** - Route definitions for authentication
- **forms.py** - WTForms definitions for authentication forms

## Routes

### Authentication Routes

- **`/login`** (`login`) - User login
  - Authenticates users
  - Handles remember-me functionality
  - Redirects based on user role
  
- **`/logout`** (`logout`) - User logout
  - Ends user session
  - Redirects to login page
  
- **`/register`** (`register`) - User registration
  - Creates new user accounts
  - Validates form input
  - Sets up initial user profile

### Profile Management

- **`/profile/edit`** (`edit_profile`) - Edit profile
  - Updates user information
  - Changes password
  - Updates profile settings
  
- **`/notifications`** (`notifications`) - User notifications
  - Displays notifications
  - Handles group invitations
  - Marks notifications as read

## Templates

The blueprint uses the following templates in `app/templates/auth/`:

- **login.html** - Login form
- **register.html** - Registration form
- **edit_profile.html** - Profile editing form
- **notifications.html** - Notifications display

## Forms

The blueprint includes several forms defined in `forms.py`:

- **LoginForm** - User login with remember-me option
- **RegistrationForm** - New user registration
- **EditProfileForm** - Profile information editing
- **ChangePasswordForm** - Password changing

## User Model

The Auth blueprint primarily interacts with the User model defined in `app/models.py`:

- **User** - Core user model with:
  - Authentication fields (username, password hash)
  - Profile fields (email, etc.)
  - Role fields (is_admin, is_group_admin)
  - Relationships to other models

## Authentication Process

1. **Registration**:
   - User submits registration form
   - Form is validated
   - Password is hashed
   - New user record is created
   - User is redirected to login

2. **Login**:
   - User submits login form
   - Credentials are validated
   - Flask-Login manages user session
   - User is redirected based on role

3. **Session Management**:
   - Flask-Login maintains user session
   - Remember-me functionality extends session
   - User load happens via user_loader

## Password Security

Passwords are secured using:
- Password hashing with Werkzeug security
- No plaintext password storage
- Password validation during login
- Secure password reset process

## Role-Based Access

The auth system supports multiple user roles:
- Regular users
- Group admins
- Site administrators

Role verification happens in route decorators across the application.

## Notifications

The notification system allows:
- System messages to users
- Group invitation handling
- Read/unread status tracking
- Notification counts in UI

## Integration

The Auth blueprint integrates with:
- Flask-Login for session management
- Main blueprint for user flow
- Admin blueprint for role management
- Module blueprint for progress association

## Development Guidelines

When extending the authentication system:

1. Add routes to `routes.py`
2. Create forms in `forms.py`
3. Add templates to `app/templates/auth/`
4. Update User model in `app/models.py` if needed
5. Implement proper validation and error handling
6. Follow security best practices

## Security Considerations

- Password reset functionality should use secure tokens
- Account lockout should be implemented for failed attempts
- Email verification should be considered for registration
- CSRF protection is enabled via Flask-WTF
- Session security is managed by Flask-Login

For more details on authentication flow and security features, refer to the technical overview document. 