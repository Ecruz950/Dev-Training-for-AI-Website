# Modules Blueprint

This directory contains the Modules blueprint which manages educational content delivery, quizzes, and progress tracking for the AI Training Platform.

## Overview

The Modules blueprint handles:
- Module listing and display
- Video content delivery
- Quiz presentation and submission
- Progress tracking and reporting

## Files

- **__init__.py** - Blueprint initialization
- **routes.py** - Route definitions for modules and quizzes

## Routes

### Module Routes

- **`/modules`** (`index`) - Lists all available modules
  - Checks user authentication
  - Displays modules with completion status
  
- **`/module/<int:module_id>`** (`module_detail`) - Shows detail for a specific module
  - Displays module information and video content
  - Shows completion status
  - Links to related quiz if available

### Quiz Routes

- **`/module/<int:module_id>/quiz`** (`quiz`) - Displays quiz for a specific module
  - Loads questions from database
  - Presents multiple-choice interface
  
- **`/module/<int:module_id>/quiz/submit`** (`submit_quiz`) - Handles quiz submission
  - Processes user answers
  - Calculates score
  - Records attempt in database
  - Updates module progress
  
- **`/module/<int:module_id>/quiz/complete`** (`quiz_complete`) - Shows quiz completion
  - Displays final score
  - Provides feedback
  - Updates module progress status

## Templates

The blueprint uses the following templates in `app/templates/modules/`:

- **index.html** - Module listing page
- **module_detail.html** - Module detail with video
- **quiz.html** - Quiz interface with questions
- **quiz_complete.html** - Quiz completion feedback

## Models

The blueprint interacts with these models (defined in `app/models.py`):

- **Module** - Contains module information and content path
- **ModuleProgress** - Tracks user progress through modules
- **Quiz** - Quiz configuration for a module
- **Question** - Individual quiz questions
- **Option** - Answer options for questions
- **QuizAttempt** - Records of user quiz attempts

## Video Content

Module videos are stored in `app/static/modules/` with defined naming conventions:
- Module videos should follow the naming pattern: `module{id}Video.mp4`
- The video path is stored in the Module model's `video_path` field

## Quiz Data

Quiz data is stored in the database, but can be initially loaded from JSON files in `app/static/quizzes/`.

Quiz JSON format:
```json
{
  "title": "Module 1 Quiz",
  "description": "Test your knowledge of Module 1",
  "questions": [
    {
      "text": "Question text?",
      "options": [
        {"text": "Option 1", "is_correct": true, "feedback": "Good job!"},
        {"text": "Option 2", "is_correct": false, "feedback": "Not quite."},
        {"text": "Option 3", "is_correct": false, "feedback": "Try again."}
      ]
    }
  ]
}
```

## Progress Tracking

Module progress is tracked using the ModuleProgress model:
- `is_completed` - Whether the module has been completed
- `completion_date` - When the module was completed
- `quiz_passed` - Whether the associated quiz was passed

## Usage Flow

1. User views list of modules at `/modules`
2. User selects a module and views content at `/module/<id>`
3. User takes the quiz at `/module/<id>/quiz`
4. User submits answers and sees results at `/module/<id>/quiz/complete`
5. Progress is updated in the database

## Development Guidelines

When extending the modules system:

1. Add routes to `routes.py`
2. Create corresponding templates in `app/templates/modules/`
3. Update models in `app/models.py` if needed
4. Use the `current_user` object for user-specific logic
5. Always update the ModuleProgress model when progress status changes

## Integration

The Modules blueprint integrates with other components:
- Authentication system for user identification
- Admin dashboard for content management
- Main blueprint for progress display on profile page

For more details on quiz implementation and content management, refer to the technical overview document. 