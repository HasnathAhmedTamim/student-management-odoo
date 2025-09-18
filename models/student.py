
# Import Odoo's base model and field types
from odoo import models, fields


# Define the Student model
class Student(models.Model):
    _name = 'student.management.student'  # Technical name for the model
    _description = 'Student'  # Human-readable description


    # Student's name (required field)
    name = fields.Char(string='Name', required=True)
    # Student's email address
    email = fields.Char(string='Email')
    # Student's roll number
    roll_no = fields.Char(string='Roll No')
    # Department the student belongs to
    department = fields.Char(string='Department')
    # Many-to-many relationship to courses (enrollments)
    course_ids = fields.Many2many('student.management.course', string='Courses')


    # Action method to show all courses a student is enrolled in
    def action_show_enrolled_courses(self):
        self.ensure_one()  # Make sure only one student record is selected
        return {
            'type': 'ir.actions.act_window',  # Open a new window
            'name': 'Enrolled Courses',  # Title of the window
            'res_model': 'student.management.course',  # Model to display
            'view_mode': 'list,form',  # Show both list and form views
            'domain': [('id', 'in', self.course_ids.ids)],  # Filter to only this student's courses
            'target': 'new',  # Open in a popup window
        }
