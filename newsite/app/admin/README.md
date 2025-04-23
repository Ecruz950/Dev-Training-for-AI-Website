# Admin Blueprint

This directory contains the Admin blueprint which provides administrative functionality for the AI Training Platform.

## Overview

The Admin blueprint provides:
- User management dashboard
- Group administration
- Module and quiz management
- Progress monitoring
- System settings

## Files

- **__init__.py** - Blueprint initialization
- **routes.py** - Route definitions for the admin dashboard

## Routes

### Dashboard Routes

- **`/admin`** (`index`) - Main admin dashboard
  - Displays system overview
  - Shows user counts and activity metrics
  
- **`/admin/users`** (`users`) - User management
  - Lists all users with role information
  - Displays progress statistics
  - Provides user management controls

- **`/admin/groups`** (`groups`) - Group management
  - Lists all groups with member counts
  - Provides group creation and editing functionality
  - Allows adding/removing group members

### User Management Routes

- **`/admin/user/<int:user_id>`** (`user_detail`) - User detail page
  - Shows user profile information
  - Displays user's module progress
  - Allows role management
  
- **`/admin/user/<int:user_id>/edit`** (`edit_user`) - Edit user
  - Allows editing user information
  - Provides role assignment
  - Can reset progress if needed

### Group Management Routes

- **`/admin/group/create`** (`create_group`) - Create new group
  - Group creation form
  - Initial member assignment
  
- **`/admin/group/<int:group_id>`** (`group_detail`) - Group detail
  - Shows group information
  - Lists members with their roles
  - Displays group progress metrics

## Templates

The blueprint uses the following templates in `app/templates/admin/`:

- **index.html** - Main admin dashboard
- **users.html** - User management page
- **user_detail.html** - Individual user detail
- **groups.html** - Group management page
- **group_detail.html** - Individual group detail
- **create_group.html** - Group creation form

## Access Control

The Admin blueprint is protected by admin role verification:
- All routes check for `current_user.is_admin` status
- Non-admin users are redirected to the main index
- Functions are decorated with custom `admin_required` decorator

## Models

The blueprint interacts with these models (defined in `app/models.py`):

- **User** - For user management and role assignment
- **Group** - For group management
- **GroupMember** - For managing group membership
- **Module** - For module management
- **ModuleProgress** - For tracking user progress
- **Quiz** - For quiz management
- **QuizAttempt** - For reviewing quiz attempts

## Data Display

The admin dashboard presents data in several ways:
- Tables for user and group listings
- Progress bars for completion statistics
- Charts for activity metrics (if implemented)
- Detailed views for individual entities

## User Management

Admin users can perform these tasks:
- Create new users
- Edit existing user information
- Assign roles (Admin, Group Admin, Regular User)
- Reset user passwords if needed
- View detailed progress information
- Delete users if necessary

## Group Management

Admin users can perform these tasks:
- Create new groups
- Add/remove members
- Assign group admins
- Edit group information
- View group progress metrics
- Delete groups if necessary

## Integration

The Admin blueprint integrates with other components:
- Authentication system for user verification
- Modules system for content management
- Main blueprint for general application flow

## Development Guidelines

When extending the admin system:

1. Add routes to `routes.py`
2. Create corresponding templates in `app/templates/admin/`
3. Update models in `app/models.py` if needed
4. Always check admin permissions with the appropriate decorator
5. Follow existing UI patterns for consistency

For security considerations and additional admin features, refer to the technical overview document. 