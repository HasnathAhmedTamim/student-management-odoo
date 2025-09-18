{
    'name': 'Student Management',
    'version': '18.0.1.0.0',
    'summary': 'Manage students and courses',
    'category': 'Tools',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student_views.xml',
        'views/course_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}