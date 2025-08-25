# -*- coding: utf-8 -*-

from odoo import fields,models,api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_studio_canal = fields.Char(string='Canal',store=True)