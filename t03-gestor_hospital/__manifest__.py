# -*- coding: utf-8 -*-
{
    'name': "Gestor Hospital  MB",

    'summary': "Gestionar un Hospital.",

    'description': """
    Módulo para gestionar los diagnosticos de los medicos y pacientes MB.
    """,

    'author': "Mohammed Benali",
    'application': True,
    'category': 'Tools',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/vista_paciente.xml',
        'views/vista_medico.xml',
        'views/vista_diagnostico.xml' 
    ],

}

