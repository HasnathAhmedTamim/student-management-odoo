# Student Management Odoo Module

## Overview
This module allows you to manage students and courses, enroll students in multiple courses, and view enrollments. Built for Odoo 18+.

## Requirements
- Odoo 18.0 or higher
- Python 3.10+

## Features
- Student and Course models
- Many-to-many relation (enrollment)
- Form and list views for both models
- Menu navigation under "Student Management"
- Enroll students in multiple courses
- View all students in a course
- Action buttons for quick navigation

## Installation
1. Copy the `student_management` folder into your Odoo `addons` directory (the path must be in your `addons_path` in `odoo.conf`).
2. Restart the Odoo server.
3. Update the app list in Odoo (Apps > Update Apps List).
4. Search for "Student Management" in the Apps menu and click Install.

## Usage
- Go to the main menu and select **Student Management > Students** to add or view students.
- Go to **Student Management > Courses** to add or view courses.
- In the student form, use the "Courses" field to enroll a student in multiple courses.
- In the course form, use the "Students" field to see all enrolled students.
- Use the action buttons to quickly view related records.

## Troubleshooting
- If the module does not appear in the Apps list, ensure the folder is in the correct `addons_path` and there are no syntax errors in the module files.
- If you see an Internal Server Error, check the Odoo log file (path set in `odoo.conf`) for details.
- Make sure your database user has the correct permissions.


## Challenges Faced and Solutions
- **Learning Odoo's ORM and XML view system:**
	- Solution: Followed Odoo documentation and community tutorials to understand model and view definitions.
- **Setting up many-to-many relationships:**
	- Solution: Used Odoo's `Many2many` field and tested with sample data to ensure enrollments worked as expected.
- **Menu and access rights configuration:**
	- Solution: Carefully structured XML files and used Odoo's security CSV to grant the right permissions.
- **Odoo 18 compatibility issues (view types, manifest version):**
	- Solution: Updated view types to `list` and manifest version to `18.0.1.0.0` as per Odoo 18 requirements.
- **Troubleshooting Internal Server Errors:**
	- Solution: Checked Odoo log files for error details and fixed issues in XML and Python files accordingly.

## Bonus (Optional)
- Add a button on the student form to show enrolled courses.
- Create a report/page to show all students in a specific course.
