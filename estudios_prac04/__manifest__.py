# -*- coding: utf-8 -*-
{
    'name': "Estudios Prac 4",

    'summary': "Representa estudios del Instituto",

    'description': """
Modulo que representa los ciclos formativos del Instituto
    """,

    'author': "Mohammed Benali",
    'application': True,
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/cicloformativo.xml',
        'views/alumno.xml',
        'views/profesor.xml',
        'views/modulo.xml'
    ],

}

