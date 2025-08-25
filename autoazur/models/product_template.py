# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_studio_cdb = fields.Char(string="CDB",store=True)
    x_studio_cdb2 = fields.Char(string="CDB2",store=True)
    x_studio_stock_drop = fields.Float(string="Stock Drop",store=True)
    

    