{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management Software',
    'sequence': 0,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://github.com/GuiBritx',
    'depends' : [
        'sale',
        'mail'
    
    ],
    'data': [
        'views/patient.xml',
        'security/ir.model.access.csv',
        'views/sale.xml',
        'data/data.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/appointment_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
