
# Import Odoo's base model and field types
from odoo import models, fields


# Define the Course model
class Course(models.Model):
    _name = 'student.management.course'  # Technical name for the model
    _description = 'Course'  # Human-readable description


    # Course name (required field)
    name = fields.Char(string='Name', required=True)
    # Course code (e.g., CS101)
    code = fields.Char(string='Code')
    # Number of credits for the course
    credit = fields.Integer(string='Credit')
    # Many-to-many relationship to students (enrollments)
    student_ids = fields.Many2many('student.management.student', string='Students')


    # Action method to show all students enrolled in this course
    def action_show_students(self):
        self.ensure_one()  # Make sure only one course record is selected
        return {
            'type': 'ir.actions.act_window',  # Open a new window
            'name': 'Enrolled Students',  # Title of the window
            'res_model': 'student.management.student',  # Model to display
            'view_mode': 'list,form',  # Show both list and form views
            'domain': [('id', 'in', self.student_ids.ids)],  # Filter to only this course's students
            'target': 'new',  # Open in a popup window
        }
