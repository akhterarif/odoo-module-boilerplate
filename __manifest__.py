# -*- coding: utf-8 -*-
{
    'name': "Example: The example module",

    'summary': """This is a boilerplate module which includes all the python and xml files for testing a module.""",

    'description': """
        This is a boilerplate module which includes all the python and xml files for testing a module.
    """,
    'author': "Akhteruzzaman Arif",
    'website': "https://github.com/akhterarif",
    "category": "*",
    'images': ['static/description/banner.png'],
    'version': '16.1.0.0',
    'license': 'GPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/example.xml',
        'views/example_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
    'installable': True
}
