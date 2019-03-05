# -*- coding: utf-8 -*-
{
    'name': "Tickets",

    'summary': """Generación de Tickets para Venta""",

    'description': """
        Módulo para la generación de tickets:
            - envío directo a la impresora de tickets
            - consulta de artículos en base al módelo y el almacén
            - configuración de la cantidad de tickets a imprimir            
    """,

    'author': "Art Atlas",
    'website': "http://www.artatlasperu.com/web/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'ArtAtlas',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}