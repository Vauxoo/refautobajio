# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReclamosMeli(models.Model):
    
    _name = "x_reclamos_meli"

    x_name = fields.Char(string="Descripción")
    x_studio_observaciones_1 = fields.Char(string="Observaciones")
    x_studio_date = fields.Date(string="Date")