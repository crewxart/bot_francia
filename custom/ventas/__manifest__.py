# -*- coding: utf-8 -*-
{
    'name': "ventas",

    'summary': """
        Módulo desarrollado para facilitar la gestión de ventas de manera local en Botillería Francia""",

    'description': """
        En este módulo se le permitirá al usuario que tenga todos los permisos
poder gestionar las ventas de la organización y ver indicadores.
    """,

    'author': "Esteban Carvallo",
    'website': "https://github.com/crewxart",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'gestion',
    'version': '0.1',
#
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}