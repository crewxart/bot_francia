# -*- coding: utf-8 -*-
{
    'name': "inventario",

    'summary': """
        Módulo de inventario para gestionar de manera local Botillería Francia""",

    'description': """
         En este módulo se le permitirá al usuario que tenga todos los permisos
poder gestionar los productos registrados
    """,

    'author': "Diego Valenzuela",
    'website': "https://github.com/Kfc33",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'gestion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_producto.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}