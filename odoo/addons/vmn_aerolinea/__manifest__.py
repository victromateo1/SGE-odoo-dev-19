# -*- coding: utf-8 -*-
{
    'name': "vmn_aerolinea",

    'summary': "Este es un módulo para la gestión de una aerolínea",

    'description': """
Este es un módulo para la gestión de una aerolínea
    """,

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'author': "Víctor Mateo Navajas",
    'website': "https://www.yourcompany.com",
    'icon': '/vmn_aerolinea/static/description/icono.png',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/grupos_seguridad.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/avion.xml',
        'views/azafata.xml',
        'views/maleta.xml',
        'views/pasajero.xml',
        'reports/report_avion.xml',
        'reports/report_pasajero.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

