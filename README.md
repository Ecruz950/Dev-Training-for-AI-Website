# Dev-Training-for-AI-Website

## Tasks to do:
- Bridging connection between the front-end and back-end of our web platform 
    - Storing login details to the database of registered users when user registers on registration page 
    - When user attempts to log in on the login page there must be some form of verification that verifies that the user is a registered user 
        - If the user is a registered user then allow user to proceed to the module dashboard 
        - Else notify the user that they are not a registered user 
    - Fetch the user’s name and email address back end and display it on the top left corner of the module dashboard page when they log in 
    - Fetch and store the module status (Incomplete, Pending, Complete), title, and cover image of each module and display it on the module dashboard page by its appropriate category (“Enrolled Modules” | ”Completed Modules”)  
        - Whenever the user completes a module or starts a module and exits it then the module status must be updated 
            - The default module status should display as “Incomplete” signifying that the user has yet to start the module 
            - If the user clicks and enters the module => update module status to “Pending” 
            - If the user follows through the module and completes the module => update module status to “Complete” and move the module to the users set of “Completed Modules” 
                - Should be updated on both the module dashboard page and the database 
    - Store users quiz progress (Answer choices) in the database?  
        - In the case that they want to revisit the module video 
    - Store module video & transcript in the database and have it fetched and displayed to the user when they proceed to the module video page? 

- Move website to the server (Done at the end when website is finished) (Assigned: Alec)

- Make sure website is responsive & secure


## What we are storing in the database
- Email, Password, and Full Name
- Quiz results
- Enrolled Modules & Completed Modules
    - Module status for each module 
