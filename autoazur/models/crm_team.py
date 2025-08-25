# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmTeam(models.Model):
    _inherit = "crm.team"

    x_studio_cdigo = fields.Char(string="Código",store=True)
    x_studio_inventario_sync = fields.Many2one('x_invubisync',string="Inventario Sync")
    x_studio_id_az = fields.Char(string="ID AZ",store=True)
    x_studio_almacn_drop = fields.Many2one('stock.warehouse', string="Almacén DROP")
    x_studio_almacn_full = fields.Many2one('stock.warehouse', string="Almacén FULL")
    x_studio_channelid = fields.Char(string="channelid", store=True)
    