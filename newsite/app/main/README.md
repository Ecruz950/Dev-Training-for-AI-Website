# Main Blueprint

This directory contains the Main blueprint which serves as the primary interface for user interaction with the AI Training Platform.

## Overview

The Main blueprint handles:
- Homepage and dashboard
- User profile page
- Group management for users
- Navigation and site structure

## Files

- **__init__.py** - Blueprint initialization
- **routes.py** - Route definitions for main application pages

## Routes

### Core Routes

- **`/`** (`index`) - Homepage/Dashboard
  - Entry point for authenticated users
  - Redirects to login if not authenticated
  - Shows personalized dashboard with progress
  
- **`/profile`** (`profile`) - User profile
  - Displays user information
  - Shows module completion progress
  - Lists group memberships
  - Provides access to notifications

### Group Management Routes

- **`/group-management`** (`group_management`) - Group management
  - For group admins to manage their groups
  - Create new groups
  - Invite members
  - View group progress
  
- **`/create-group`** (`create_group`) - Create group
  - Form for creating a new group
  - Initial settings configuration
  
- **`/invite-to-group/<int:group_id>`** (`invite_to_group`) - Send invitations
  - Email invitation functionality
  - Member management interface
  
- **`/remove-from-group/<int:group_id>/<int:user_id>`** (`remove_from_group`) - Remove members
  - Remove users from a group
  - Permission verification

## Templates

The blueprint uses the following templates in `app/templates/main/`:

- **index.html** - Homepage/Dashboard
- **profile.html** - User profile page
- **group_management.html** - Group management interface
- **create_group.html** - Group creation form
- **invite.html** - Group invitation form

## Integration

The Main blueprint serves as the central hub connecting all other components:

- Links to Module blueprint for learning content
- Accesses Auth blueprint for user management
- Connects to Admin blueprint for administrative users
- Provides navigation to all platform features

## Dashboard Features

The main dashboard includes:
- Progress overview for modules
- Quick links to content
- Notification indicators
- Group membership information

## Profile Features

The profile page displays:
- User account information
- Progress bars for module completion
- List of group memberships
- Quick links to learning modules

## Group Management Features

Group management pages provide:
- Group creation for eligible users
- Member invitation through email
- Group progress overview
- Member management tools

## Navigation

The main blueprint manages the primary navigation through:
- Sidebar menu in base template
- Navigation links in header
- Breadcrumb navigation where appropriate
- Responsive menu for mobile devices

## Role-Based Features

The blueprint adapts content based on user roles:
- Regular users see basic profile and module access
- Group admins see group management features
- Administrators see links to admin dashboard

## Development Guidelines

When extending the main blueprint:

1. Add routes to `routes.py`
2. Create templates in `app/templates/main/`
3. Update navigation in `base.html` if needed
4. Consider role-based access requirements
5. Maintain consistent UI patterns
6. Ensure proper integration with other blueprints

## User Experience Flow

The typical user flow through the main blueprint:
1. User logs in and sees the dashboard
2. User navigates to profile to view progress
3. User accesses learning modules from dashboard
4. Group admins manage their groups via group management
5. Admin users access admin dashboard through navigation

For more details on interface design and user flow, refer to the technical overview document. 