# -*- coding: utf-8 -*-
{
    'name': "Autoazur",

    'summary': """
        Autoazur""",

    'description': """
        Módulo de conexión con Autoazur
    """,

    'author': "Millora",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_management','sales_team','product','stock','base_automation','crm','mrp'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/override_crm_team_views.xml',
        'views/override_product_views.xml',
        'views/override_sale_order_views.xml',
        'views/override_stock_picking_view.xml',
        'views/override_res_partner_views.xml',
         'views/stopper_views.xml',
         'views/reclamos_meli_views.xml',
        'data/base_automation.xml',
        'data/invubisync_data.xml',
        'data/ir_cron_data.xml',
        'data/product_data.xml',
        'data/stopper_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
